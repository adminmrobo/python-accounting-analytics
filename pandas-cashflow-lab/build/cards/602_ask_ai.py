from lib import *
from snippets import SAMPLE_REPLY

CARD = dict(
    id="ask_ai", ch="6. 생성AI 에게 맡기기", cmd="client.models.generate_content()",
    title="파이썬에서 생성AI 를 불러 답을 받는다", excel="(해당 없음) 채팅창에 붙여 넣고 답 복사하기",
    desc="채팅창에 붙여 넣는 일을 코드로 한다. Google AI Studio(aistudio.google.com)에서 API 키를 발급받아 google-genai 라이브러리로 부른다. "
         "함수 ask_ai 는 프롬프트를 보내고 답 글자를 돌려준다. response_mime_type 을 JSON 으로 주면 답이 JSON 으로만 온다. "
         "키가 없어도 연습할 수 있게 USE_API = False 이면 저장해 둔 예시 응답을 돌려준다. 아래 실행 결과는 이 예시 응답이며, 실제 AI 의 답은 부를 때마다 조금씩 다를 수 있다.",
    code="# 실제로 부르려면 새 셀에서 먼저:  !pip -q install google-genai\n" + SAMPLE_REPLY + '''

USE_API = False                      # 키를 넣고 True 로 바꾸면 실제로 부른다
API_KEY = ""                         # Google AI Studio 에서 발급. 코드에 적은 채로 공유하지 않는다
MODEL = "gemini-3.6-flash"           # AI Studio 모델 목록에 있는 이름으로 바꾼다

def ask_ai(prompt):
    if not USE_API:
        return SAMPLE_REPLY          # 저장해 둔 예시 응답
    from google import genai
    client = genai.Client(api_key=API_KEY)
    resp = client.models.generate_content(model=MODEL, contents=prompt,
                                          config={"response_mime_type": "application/json"})
    return resp.text

reply = ask_ai("(601 카드에서 만든 prompt 를 넣는다)")
print(type(reply), len(reply), "글자")
print(reply[:230])''',
    tip="다른 회사의 AI 를 써도 ask_ai 함수 안만 바꾸면 된다. 프롬프트를 보내고 글자를 받는다는 구조는 같다. PDF 가 스캔본이면 client.files.upload(file=\"report.pdf\") 로 파일을 올리고 contents=[올린 파일, prompt] 로 함께 보낸다. 모델 이름과 무료 한도는 자주 바뀌니 AI Studio 화면에서 확인한다.",
    talk=[dict(who="fly", text="API 키를 코드에 적은 채로 깃허브에 올리면 안 돼. 남이 써.")],
)

def stages(ns, out):
    return [
        S("프롬프트", "601 카드에서 만든 글자 하나를 보낸다.", TX("PROMPT\n + 재무상태표 csv\n + 손익계산서 csv", "code", "prompt")),
        S("ask_ai()", "키가 있으면 Gemini 를 부르고, 없으면 예시 응답을 돌려준다.",
          TX("USE_API = True  → generate_content()\nUSE_API = False → SAMPLE_REPLY", "code", "갈림길")),
        S("답은 글자", "돌아온 것은 표가 아니라 JSON 모양의 글자다. 앞뒤에 ```json 울타리가 붙어 오기도 한다. 다음 카드에서 표로 바꾼다.",
          TX(ns["reply"][:300] + "\n…", "out", "reply")),
    ]
