from lib import *

CARD = dict(
    id="secrets", ch="7. 앱으로 만들기", cmd='os.environ.get("GEMINI_API_KEY")',
    title="API 키는 코드 밖에 둔다", excel="(해당 없음) 비밀번호를 시트에 적지 않기",
    desc="API 키는 비밀번호다. 코드에 적은 채 깃허브에 올리면 누구나 가져다 쓸 수 있고, 요금이 나올 수 있다. "
         "키를 두는 곳은 셋이다. ① 화면의 입력 칸(이 책의 app.py 방식. 쓸 때마다 넣는다) ② 환경변수 ③ Streamlit 의 secrets 파일. "
         "코드에서는 os.environ.get 으로 읽고, 없으면 빈 글자를 받는다. .gitignore 파일에 secrets 파일 이름을 적어 두면 깃이 그 파일을 올리지 않는다.",
    code='''import os

# 연습: 환경변수에 가짜 키를 넣고 읽어 본다 (실제 키는 코드에 적지 않는다)
os.environ["GEMINI_API_KEY"] = "abcd1234-example-key"
key = os.environ.get("GEMINI_API_KEY", "")
print("키를 찾았다:", bool(key), "| 끝 네 글자:", key[-4:])
print("없는 이름:", repr(os.environ.get("NO_SUCH_KEY", "")))

# 깃허브에 올리지 않을 파일 목록
with open(".gitignore", "w") as f:
    f.write(".streamlit/secrets.toml\\n.env\\n__pycache__/\\n")
print(open(".gitignore").read())''',
    tip='Streamlit Community Cloud 에서는 앱 설정의 Secrets 칸에 GEMINI_API_KEY = "..." 를 적고, 코드에서 st.secrets["GEMINI_API_KEY"] 로 읽는다. 과제용 앱은 내 키를 넣어 두지 말고 사용자가 자기 키를 입력 칸에 넣게 한다. 키가 새어 나갔다면 AI Studio 에서 그 키를 지우고 새로 발급한다.',
    talk=[dict(who="fly", text="키를 화면에 전부 출력하지 마. 끝 네 글자만 확인해.")],
)

def stages(ns, out):
    import pandas as pd
    t = pd.DataFrame({"두는 곳": ["화면 입력 칸", "환경변수", "secrets 파일"],
                      "읽는 코드": ['st.text_input(type="password")', 'os.environ.get("GEMINI_API_KEY")', 'st.secrets["GEMINI_API_KEY"]'],
                      "맞는 경우": ["과제 · 여러 사람이 쓰는 앱", "내 PC", "클라우드에 올린 나만의 앱"]})
    lines = out.splitlines()
    return [
        S("세 곳", "코드 파일 안은 어디에도 없다.", T(t)),
        S("환경변수 읽기", "있으면 값을, 없으면 빈 글자를 받는다.", TX("\n".join(lines[:2]), "out", "출력")),
        S(".gitignore", "여기 적힌 파일은 깃허브에 올라가지 않는다.", TX("\n".join(lines[2:]), "code", ".gitignore")),
    ]
