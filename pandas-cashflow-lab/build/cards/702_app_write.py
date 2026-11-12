from lib import *
from make_app import app_source

CARD = dict(
    id="app_write", ch="7. 앱으로 만들기", cmd="streamlit: app.py 한 파일",
    title="화면이 있는 앱으로 만든다", excel="버튼과 입력 칸을 단 매크로 통합 문서",
    desc="Streamlit 은 파이썬 파일 하나로 웹 화면을 만들어 주는 라이브러리다. st.file_uploader 는 파일 올리기 칸, st.data_editor 는 고칠 수 있는 표, "
         "st.download_button 은 내려받기 버튼이다. app.py 는 지금까지 만든 것을 순서대로 잇는다. "
         "① 파일 읽기(5장) → ② 표 정리: 규칙 사전(5장) 또는 생성AI(6장) → ③ 사람이 숫자와 분류를 검토하고 고침 → ④ make_cashflow 계산 → ⑤ 검산 → ⑥ 엑셀 내려받기. "
         "아래 코드는 app.py 전체를 파일로 써 주고 문법만 확인한다. 화면을 띄우는 방법은 다음 카드에 있다.",
    code="APP = r'''" + app_source() + "'''\n" + '''
import ast

with open("app.py", "w", encoding="utf-8") as f:
    f.write(APP)
tree = ast.parse(APP)                                    # 문법 확인
funcs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
print("app.py", len(APP.splitlines()), "줄")
print("함수:", funcs)''',
    tip="③ 단계가 이 앱의 핵심이다. AI 의 답을 바로 계산에 넣지 않고 사람이 고칠 수 있는 표로 먼저 보여 준다. 고치면 아래의 현금흐름표와 검산이 즉시 다시 계산된다. 저장소의 app/app.py 가 같은 파일이다.",
    talk=[
        dict(who="asst", text="AI 가 읽은 표를 왜 사람이 다시 봐요?"),
        dict(who="doc", text="책임은 사람이 지니까요. 고칠 수 있는 칸을 꼭 둬요."),
    ],
)

def stages(ns, out):
    import pandas as pd
    flow = pd.DataFrame({
        "단계": ["① 파일 읽기", "② 표 정리", "③ 사람 검토", "④ 계산", "⑤ 검산", "⑥ 내려받기"],
        "함수": ["read_tables", "tidy_pl · tidy_bs 또는 ask_ai · parse_reply", "st.data_editor", "make_cashflow", "make_cashflow 의 검산표", "to_excel_bytes"],
        "배운 곳": ["5장", "5장 · 6장", "7장", "2~4장 · 7장", "4장 · 7장", "7장"],
    })
    scr = pd.DataFrame({
        "화면 요소": ["왼쪽 설정", "파일 올리기", "원본 표", "정리된 표 두 장", "숫자 카드 네 개", "현금흐름표", "검산표", "내려받기 버튼"],
        "Streamlit 명령": ["st.sidebar · st.radio · st.text_input", "st.file_uploader", "st.expander · st.dataframe", "st.data_editor", "st.metric", "st.dataframe", "st.dataframe · st.success", "st.download_button"],
    })
    return [
        S("여섯 단계", "앞 장에서 만든 함수를 순서대로 잇는다.", T(flow, rcls=["", "g0", "hr", "", "", ""])),
        S("화면 구성", "단계마다 화면 요소가 하나씩 있다.", T(scr)),
        S("app.py", "파일이 만들어지고 문법 확인을 통과했다.", TX(out, "out", "출력")),
    ]
