from lib import *

CARD = dict(
    id="ai_vs_rule", ch="6. 생성AI 에게 맡기기", cmd='a.merge(b, on="계정과목", suffixes=)',
    title="AI 의 분류와 사전의 분류를 나란히 놓고 다른 줄만 본다", excel="VLOOKUP 으로 옆에 붙이고 =A2=B2",
    desc="AI 의 분류가 맞는지 사람이 전부 볼 수는 없다. 낱말 사전의 분류와 merge 로 나란히 붙이고, 둘이 다른 줄만 골라 사람이 판단한다. "
         "suffixes 는 이름이 겹치는 열에 붙일 꼬리표다. 둘이 같다고 반드시 맞는 것은 아니지만, 검토할 줄 수가 크게 줄어든다. "
         "아래에서 개발비는 사전이 몰랐던 것을 AI 가 투자로 분류했고, 장기대여금은 AI 가 영업으로 잘못 분류했다.",
    code='''import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

ai = pd.DataFrame({"계정과목": ["매출채권", "미수금", "개발비", "장기대여금", "단기차입금", "선수수익"],
                   "분류": ["영업", "영업", "투자", "영업", "재무", "영업"]})
rule = pd.DataFrame({"계정과목": ["매출채권", "미수금", "개발비", "장기대여금", "단기차입금", "선수수익"],
                     "분류": ["영업", "영업", "미분류", "투자", "재무", "영업"]})

both = ai.merge(rule, on="계정과목", suffixes=("_AI", "_사전"))
both["같은가"] = both["분류_AI"] == both["분류_사전"]
print(both)
review = both[~both["같은가"]]
print("사람이 볼 줄:", review["계정과목"].tolist())''',
    tip="과제에서는 이 표를 보고서에 넣는다. AI 와 사전이 달랐던 계정, 내가 어느 쪽을 골랐는지, 그 이유(주석의 어느 부분을 봤는지)를 적는다.",
    talk=[dict(who="fly", text="대여금은 빌려준 돈이야. 영업이 아니라 투자지.")],
)

def stages(ns, out):
    both = ns["both"]
    return [
        S("두 분류", "왼쪽은 AI 의 답, 오른쪽은 낱말 사전의 결과다.", T(ns["ai"], title="ai"), T(ns["rule"], title="rule")),
        S("merge", "계정과목으로 나란히 붙이고 같은지 비교한다.",
          T(both, rcls=["ok" if s else "bad" for s in both["같은가"]], hl=("같은가",)), links=[[0, 0], [1, 0]]),
        S("다른 줄만", "여섯 줄 중 두 줄만 사람이 보면 된다.", T(ns["review"][["계정과목", "분류_AI", "분류_사전"]], rcls=["bad", "bad"])),
    ]
