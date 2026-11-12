"""app/app.py 와 연습 파일(data/)을 만든다. 페이지의 코드와 같은 문자열(snippets.py)에서 조립한다.
usage: python build/make_app.py"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))
from snippets import RAW, TOOLS, ENGINE, PROMPT

HEAD = '''# 현금흐름표 자동 작성 앱 (간접법)
# 실행:  pip install -r requirements.txt  →  streamlit run app.py
# 흐름:  파일 읽기 → 표 정리(규칙 사전 또는 생성AI) → 사람이 검토·수정 → pandas 계산 → 검산 → 엑셀 내려받기
import io
import json
'''

UI = '''
BS_KINDS = ["현금", "영업", "투자", "비현금", "재무", "이익잉여금", "미분류"]
PL_KINDS = ["일반", "비현금비용", "처분손익"]


def demo_tables():
    """연습 자료: (주)SG화학 2014년. 공시처럼 소계·쉼표·괄호가 섞인 원본 모양"""
__DEMO__
    return [raw_pl, raw_bs]


def read_tables(file):
    """올린 파일 → (원본 표 목록, 생성AI 에 보낼 글자)"""
    if file.name.lower().endswith(".pdf"):
        import pdfplumber
        tables, pages = [], []
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                pages.append(page.extract_text() or "")
                tables += [pd.DataFrame(t[1:], columns=t[0]) for t in page.extract_tables() if len(t) > 1]
        return tables, "\\n".join(pages)
    sheets = pd.read_excel(file, sheet_name=None, dtype=str)
    tables = list(sheets.values())
    return tables, "\\n\\n".join(t.to_csv(index=False) for t in tables)


def split_tables(tables):
    """표 목록에서 손익계산서와 재무상태표를 찾는다 (규칙 사전 방법)"""
    pl_raw = bs_raw = None
    for t in tables:
        words = "".join(t.iloc[:, 0].astype(str)).replace(" ", "")
        if "자산총계" in words:
            bs_raw = t
        elif "매출" in words:
            pl_raw = t
    return pl_raw, bs_raw


def ask_ai(text, key, model):
    """생성AI(Gemini)에게 표를 읽고 분류해 달라고 한다. 답은 JSON 글자"""
    from google import genai
    client = genai.Client(api_key=key)
    resp = client.models.generate_content(model=model, contents=PROMPT + text,
                                          config={"response_mime_type": "application/json"})
    return resp.text


def parse_reply(reply):
    """AI 의 답(JSON 글자) → (pl, bs). 열이 빠졌으면 여기서 오류가 난다"""
    body = re.sub(r"^```(?:json)?|```$", "", reply.strip(), flags=re.M).strip()
    data = json.loads(body)
    pl = pd.DataFrame(data["pl"])[["계정과목", "금액", "분류"]]
    bs = pd.DataFrame(data["bs"])[["계정과목", "구분", "기초", "기말", "분류"]]
    return pl, bs


def to_excel_bytes(cf, checks, pl, bs):
    buf = io.BytesIO()
    with pd.ExcelWriter(buf) as w:
        cf.to_excel(w, sheet_name="현금흐름표", index=False)
        checks.to_excel(w, sheet_name="검산", index=False)
        pl.to_excel(w, sheet_name="손익계산서(정리)", index=False)
        bs.to_excel(w, sheet_name="재무상태표(정리)", index=False)
    return buf.getvalue()


def main():
    import streamlit as st
    st.set_page_config(page_title="현금흐름표 자동 작성", layout="wide")
    st.title("현금흐름표 자동 작성 (간접법)")
    st.caption("손익계산서와 재무상태표(기초·기말)가 든 엑셀·PDF 를 올리면 간접법 현금흐름표를 만든다. 교육용이며 회계 자문이 아니다.")

    with st.sidebar:
        st.header("설정")
        mode = st.radio("표를 읽는 방법", ["규칙 사전", "생성AI"], help="규칙 사전은 연습 파일과 같은 양식만 읽는다")
        key = st.text_input("Gemini API 키", type="password", help="생성AI 방법에서만 쓴다. 화면에 저장되지 않는다")
        model = st.text_input("모델 이름", "gemini-3.6-flash", help="Google AI Studio 의 모델 목록에 있는 이름으로 바꾼다")
        demo = st.checkbox("연습 자료(SG화학 2014)로 해 보기")

    file = None if demo else st.file_uploader("재무제표 파일 (xlsx 또는 pdf)", type=["xlsx", "pdf"])
    if not demo and file is None:
        st.info("파일을 올리거나 왼쪽에서 '연습 자료로 해 보기' 를 켠다.")
        st.stop()

    # 1. 파일 읽기
    if demo:
        tables = demo_tables()
        text, source = "\\n\\n".join(t.to_csv(index=False) for t in tables), "demo"
    else:
        tables, text = read_tables(file)
        source = file.name
    with st.expander("1. 파일에서 읽은 원본", expanded=False):
        for t in tables:
            st.dataframe(t, hide_index=True)
        if not tables:
            st.text(text[:3000])

    # 2. 표 정리: 규칙 사전 또는 생성AI
    try:
        if mode == "생성AI":
            if not key:
                st.warning("왼쪽에 API 키를 넣는다.")
                st.stop()
            if st.session_state.get("ai_source") != (source, model):
                with st.spinner("생성AI 가 표를 읽는 중"):
                    st.session_state["ai_reply"] = ask_ai(text, key, model)
                    st.session_state["ai_source"] = (source, model)
            with st.expander("생성AI 의 답 (원문)"):
                st.code(st.session_state["ai_reply"], language="json")
            pl, bs = parse_reply(st.session_state["ai_reply"])
        else:
            pl_raw, bs_raw = split_tables(tables)
            if pl_raw is None or bs_raw is None:
                st.error("손익계산서나 재무상태표를 찾지 못했다. 양식이 다르면 '생성AI' 방법을 쓴다.")
                st.stop()
            pl, bs = tidy_pl(pl_raw), tidy_bs(bs_raw)
    except Exception as e:
        st.error(f"표를 정리하지 못했다: {e}")
        st.stop()

    # 3. 사람이 검토하고 고친다
    st.subheader("2. 정리된 표: 숫자와 분류를 직접 고칠 수 있다")
    c1, c2 = st.columns(2)
    c1.markdown("**손익계산서** (비용은 음수)")
    pl = c1.data_editor(pl, hide_index=True, key="pl_" + source, column_config={
        "분류": st.column_config.SelectboxColumn(options=PL_KINDS, required=True)})
    c2.markdown("**재무상태표**")
    bs = c2.data_editor(bs, hide_index=True, key="bs_" + source, column_config={
        "구분": st.column_config.SelectboxColumn(options=["자산", "부채", "자본"], required=True),
        "분류": st.column_config.SelectboxColumn(options=BS_KINDS, required=True)})

    # 4. 계산과 검산
    try:
        cf, checks = make_cashflow(pl, bs)
    except Exception as e:
        st.error(f"계산하지 못했다: {e}")
        st.stop()
    total = cf.groupby("활동", sort=False)["금액"].sum()
    st.subheader("3. 현금흐름표")
    cols = st.columns(4)
    for col, act in zip(cols, ["영업활동", "투자활동", "재무활동"]):
        col.metric(act, f"{int(total.get(act, 0)):,}")
    cols[3].metric("현금의 증가", f"{int(cf['금액'].sum()):,}")
    st.dataframe(cf, hide_index=True, width=700)

    st.subheader("4. 검산")
    st.dataframe(checks, hide_index=True, width=700)
    if checks["통과"].all():
        st.success("검산 네 가지를 모두 통과했다.")
    else:
        st.error("통과하지 못한 검산이 있다. 위 표에서 숫자나 분류를 고친다.")

    st.download_button("엑셀로 내려받기", to_excel_bytes(cf, checks, pl, bs), "cashflow.xlsx")


if __name__ == "__main__":
    main()
'''

def app_source():
    demo = RAW.split("\n\n", 1)[1]                      # import·set_option 줄 뒤의 표 두 개
    demo = "\n".join("    " + l if l else l for l in demo.splitlines())
    return (HEAD + TOOLS + "\n\n\n" + ENGINE + "\n\n\n" + PROMPT + "\n\n" + UI.replace("__DEMO__", demo))

def make_data():
    import pandas as pd
    ns = {}
    exec(RAW, ns)
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    x = os.path.join(ROOT, "data", "sg_2014.xlsx")
    with pd.ExcelWriter(x) as w:
        ns["raw_pl"].to_excel(w, sheet_name="손익계산서", index=False)
        ns["raw_bs"].to_excel(w, sheet_name="재무상태표", index=False)
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.platypus import SimpleDocTemplate, Spacer, Table
    pdfmetrics.registerFont(UnicodeCIDFont("HYGothic-Medium"))
    style = [("FONTNAME", (0, 0), (-1, -1), "HYGothic-Medium"), ("GRID", (0, 0), (-1, -1), 0.5, (0, 0, 0))]
    rows = lambda df: [list(df.columns)] + df.fillna("").values.tolist()
    SimpleDocTemplate(os.path.join(ROOT, "data", "sg_2014.pdf"), pagesize=A4).build(
        [Table(rows(ns["raw_bs"]), style=style), Spacer(1, 20), Table(rows(ns["raw_pl"]), style=style)])

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "app"), exist_ok=True)
    open(os.path.join(ROOT, "app", "app.py"), "w", encoding="utf-8").write(app_source())
    open(os.path.join(ROOT, "app", "requirements.txt"), "w").write("streamlit\npandas\nopenpyxl\npdfplumber\ngoogle-genai\n")
    make_data()
    print("app/app.py", len(app_source().splitlines()), "lines; data/sg_2014.xlsx, data/sg_2014.pdf")
