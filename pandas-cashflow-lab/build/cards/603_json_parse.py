from lib import *
from snippets import SAMPLE_REPLY

CARD = dict(
    id="json_parse", ch="6. 생성AI 에게 맡기기", cmd="pd.DataFrame(json.loads(글자))",
    title="AI 의 답을 표로 바꾼다", excel="텍스트 나누기",
    desc="AI 의 답은 글자다. 앞뒤의 ```json 울타리를 정규식으로 떼고 json.loads 에 넣으면 파이썬 사전이 된다. "
         'data["bs"] 는 사전의 리스트이고, 사전의 리스트는 pd.DataFrame 에 넣으면 그대로 표가 된다. '
         "열을 이름으로 다시 골라 두면, AI 가 열을 빠뜨렸을 때 여기서 바로 오류가 난다.",
    code=SAMPLE_REPLY + '''
import json
import re
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

reply = SAMPLE_REPLY
body = re.sub(r"^```(?:json)?|```$", "", reply.strip(), flags=re.M).strip()   # 울타리 떼기
data = json.loads(body)
print(type(data), list(data))

pl = pd.DataFrame(data["pl"])[["계정과목", "금액", "분류"]]
bs = pd.DataFrame(data["bs"])[["계정과목", "구분", "기초", "기말", "분류"]]
print(bs)
print(bs.dtypes.tolist())''',
    tip="json.loads 가 JSONDecodeError 를 내면 AI 가 JSON 이 아닌 글을 섞은 것이다. print(reply) 로 원문을 보고, 프롬프트에 'JSON 으로만 답하라' 를 다시 강조하거나 한 번 더 부른다.",
)

def stages(ns, out):
    return [
        S("글자", "```json 울타리 안에 JSON 이 들어 있다.", TX(ns["reply"][:210] + "\n…", "code", "reply")),
        S("json.loads", "울타리를 떼고 읽으면 키가 pl, bs 인 사전이다. 값은 사전의 리스트다.",
          TX(str(ns["data"]["bs"][:2]).replace("}, {", "},\n {"), "out", 'data["bs"][:2]')),
        S("DataFrame", "사전의 리스트가 표가 된다. 기초와 기말은 숫자(int64)로 들어왔다.", T(ns["bs"], hl=("분류",))),
    ]
