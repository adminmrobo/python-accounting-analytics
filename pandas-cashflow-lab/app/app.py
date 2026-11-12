# 현금흐름표 자동 작성 앱 (간접법)
# 실행:  pip install -r requirements.txt  →  streamlit run app.py
# 흐름:  파일 읽기 → 표 정리(규칙 사전 또는 생성AI) → 사람이 검토·수정 → pandas 계산 → 검산 → 엑셀 내려받기
import io
import json
import re
import pandas as pd

SUBTOTAL = ["매출총이익", "판매비와관리비", "영업이익", "영업외수익", "영업외비용", "법인세비용차감전순이익",
            "당기순이익", "유동자산", "비유동자산", "자산총계", "유동부채", "비유동부채", "부채총계",
            "자본총계", "부채와자본총계"]
RULE_BS = {"현금": "현금", "누계액": "비현금", "매출채권": "영업", "재고": "영업", "선급": "영업", "미수": "영업",
           "매입채무": "영업", "미지급": "영업", "선수": "영업", "예수": "영업",
           "유형자산": "투자", "무형자산": "투자", "금융자산": "투자", "대여금": "투자", "보증금": "투자",
           "차입금": "재무", "사채": "재무", "자본금": "재무", "주식발행초과금": "재무",
           "이익잉여금": "이익잉여금", "결손금": "이익잉여금"}
RULE_PL = {"상각비": "비현금비용", "처분이익": "처분손익", "처분손실": "처분손익"}

def clean_name(s):
    """'Ⅱ. 매출채권 (주석3)' → '매출채권'"""
    s = re.sub(r"\(주석[^)]*\)", "", str(s))                  # 주석 번호
    s = re.sub(r"^\s*[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ0-9]+\s*[.)]\s*", "", s)   # 앞 번호
    return s.replace(" ", "")

def to_num(v):
    """'1,600' → 1600, '(280)' → -280, '△30' → -30, '-' → 0"""
    s = str(v).strip().replace(",", "")
    if s in ("", "-", "nan", "None", "<NA>"):
        return 0
    neg = s[0] in "(△-"
    n = int(float(re.sub(r"[()△-]", "", s)))
    return -n if neg else n

def by_rule(name, rule, default):
    """이름에 낱말이 들어 있으면 그 분류. 앞에 적은 규칙이 먼저다"""
    for word, kind in rule.items():
        if word in name:
            return kind
    return default

def tidy_pl(raw):
    """손익계산서 원본(과목, 당기) → [계정과목, 금액, 분류]. 비용은 음수"""
    t = raw.iloc[:, :2].copy()
    t.columns = ["계정과목", "금액"]
    t["계정과목"] = t["계정과목"].map(clean_name)
    t = t[~t["계정과목"].isin(SUBTOTAL)].copy()               # 소계 줄은 버린다
    t["금액"] = t["금액"].map(to_num)
    plus = t["계정과목"].str.contains("매출액|수익|이익")        # 수익이면 +, 나머지는 비용
    t["금액"] = t["금액"].where(plus, -t["금액"])
    t["분류"] = t["계정과목"].map(lambda s: by_rule(s, RULE_PL, "일반"))
    return t.reset_index(drop=True)

def tidy_bs(raw):
    """재무상태표 원본(과목, 당기말, 전기말) → [계정과목, 구분, 기초, 기말, 분류]"""
    t = raw.iloc[:, :3].copy()
    t.columns = ["계정과목", "기말", "기초"]
    t = t.replace("", pd.NA)
    t["계정과목"] = t["계정과목"].map(clean_name)
    head = t["기말"].isna()                                   # 숫자가 없는 줄 = '자산' '부채' '자본' 머리말
    t["구분"] = t["계정과목"].where(head).ffill()
    t = t[~head & ~t["계정과목"].isin(SUBTOTAL)].copy()
    t["기초"] = t["기초"].map(to_num)
    t["기말"] = t["기말"].map(to_num)
    t["분류"] = t["계정과목"].map(lambda s: by_rule(s, RULE_BS, "미분류"))
    return t[["계정과목", "구분", "기초", "기말", "분류"]].reset_index(drop=True)


def make_cashflow(pl, bs):
    """pl [계정과목, 금액, 분류] + bs [계정과목, 구분, 기초, 기말, 분류] → (현금흐름표, 검산표)"""
    bs = bs.copy()
    bs["증감"] = bs["기말"] - bs["기초"]
    # 자산이 늘면 현금 −, 부채·자본이 늘면 현금 +
    bs["현금효과"] = bs["증감"].where(bs["구분"] != "자산", -bs["증감"])
    ni = pl["금액"].sum()

    def part(df, kind, act, head, col, sign=1, tail=""):
        t = df[df["분류"] == kind]
        return pd.DataFrame({"활동": act, "항목": head + t["계정과목"] + tail, "금액": sign * t[col]})

    gain = pl.loc[pl["분류"] == "처분손익", "금액"].sum()
    re_change = bs.loc[bs["분류"] == "이익잉여금", "증감"].sum()
    cf = pd.concat([
        pd.DataFrame({"활동": ["영업활동"], "항목": ["① 당기순이익"], "금액": [ni]}),
        part(pl, "비현금비용", "영업활동", "② ", "금액", -1, " 가산"),
        part(pl, "처분손익", "영업활동", "③ ", "금액", -1, " 되돌림"),
        part(bs, "영업", "영업활동", "④ ", "현금효과", 1, " 증감"),
        part(bs, "투자", "투자활동", "", "현금효과", 1, " 순증감"),
        pd.DataFrame({"활동": ["투자활동"], "항목": ["처분손익 (영업에서 옮김)"], "금액": [gain]}),
        part(bs, "재무", "재무활동", "", "현금효과", 1, " 순증감"),
        pd.DataFrame({"활동": ["재무활동"], "항목": ["배당금 지급 (이익잉여금 역산)"], "금액": [re_change - ni]}),
    ], ignore_index=True)
    cf = cf[(cf["금액"] != 0) | (cf["항목"] == "① 당기순이익")].reset_index(drop=True)

    side = bs.groupby("구분")[["기초", "기말"]].sum()
    gap = (side.loc["자산"] - side.drop("자산").sum()).abs().sum()
    cash = bs.loc[bs["분류"] == "현금", "증감"].sum()
    noncash_bs = bs.loc[bs["분류"] == "비현금", "현금효과"].sum()
    noncash_pl = -pl.loc[pl["분류"] == "비현금비용", "금액"].sum()
    checks = pd.DataFrame([
        ("A 대차 일치 (자산 = 부채 + 자본)", gap, 0),
        ("B 미분류 계정 수", (bs["분류"] == "미분류").sum(), 0),
        ("C 세 활동 합계 = 현금 증감", cf["금액"].sum(), cash),
        ("D 비현금비용 = 비현금 계정 증감", noncash_pl, noncash_bs),
    ], columns=["검산", "계산값", "기준값"])
    checks["통과"] = checks["계산값"] == checks["기준값"]
    return cf, checks


PROMPT = """너는 회계 담당자다. 아래 [자료]에서 손익계산서와 재무상태표를 찾아 JSON 으로만 답하라.

[규칙]
1. 금액은 원 단위 정수. 쉼표를 빼고, 괄호나 △ 는 음수로 바꾼다.
2. 손익계산서: 수익은 양수, 비용은 음수. 소계(매출총이익, 영업이익, 당기순이익 등)는 넣지 않는다.
3. 재무상태표: 총계·소계는 넣지 않는다. 감가상각누계액은 음수 그대로 둔다. 구분은 자산·부채·자본 중 하나.
4. 분류 (손익): 일반 / 비현금비용(감가상각비 등) / 처분손익(자산 처분이익·손실)
5. 분류 (재무상태표): 현금 / 영업 / 투자 / 비현금(누계액) / 재무 / 이익잉여금. 모르면 미분류.
6. 자료에 없는 숫자는 만들지 않는다. 계산하지 말고 적힌 숫자만 옮긴다.

[출력 형식]
{"pl": [{"계정과목": "", "금액": 0, "분류": ""}],
 "bs": [{"계정과목": "", "구분": "", "기초": 0, "기말": 0, "분류": ""}]}

[자료]
"""


BS_KINDS = ["현금", "영업", "투자", "비현금", "재무", "이익잉여금", "미분류"]
PL_KINDS = ["일반", "비현금비용", "처분손익"]


def demo_tables():
    """연습 자료: (주)SG화학 2014년. 공시처럼 소계·쉼표·괄호가 섞인 원본 모양"""
    raw_pl = pd.DataFrame({
        "과 목": ["Ⅰ. 매출액", "Ⅱ. 매출원가", "Ⅲ. 매출총이익", "Ⅳ. 판매비와관리비", "  보험료", "  급여",
                 "  감가상각비", "  기타영업비용", "Ⅴ. 영업이익", "Ⅵ. 영업외수익", "  무형자산처분이익",
                 "Ⅶ. 영업외비용", "  이자비용", "Ⅷ. 당기순이익"],
        "당기": ["2,100", "1,100", "1,000", "810", "80", "550", "80", "100", "190", "10", "10", "30", "30", "170"],
    })
    raw_bs = pd.DataFrame({
        "과 목": ["자산", "Ⅰ. 현금및현금성자산", "Ⅱ. 매출채권 (주석3)", "Ⅲ. 상품재고", "Ⅳ. 선급보험료", "Ⅴ. 유형자산 (주석4)",
                 "  감가상각누계액", "Ⅵ. 무형자산", "자산총계", "부채", "Ⅰ. 매입채무", "Ⅱ. 미지급급여", "Ⅲ. 차입금 (주석5)",
                 "부채총계", "자본", "Ⅰ. 자본금", "Ⅱ. 이익잉여금", "자본총계", "부채와자본총계"],
        "당기말": [None, "400", "330", "220", "30", "1,600", "(280)", "200", "2,500", None, "140", "70", "730",
                  "940", None, "1,000", "560", "1,560", "2,500"],
        "전기말": [None, "250", "230", "280", "10", "1,000", "(200)", "290", "1,860", None, "100", "20", "300",
                  "420", None, "1,000", "440", "1,440", "1,860"],
    })
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
        return tables, "\n".join(pages)
    sheets = pd.read_excel(file, sheet_name=None, dtype=str)
    tables = list(sheets.values())
    return tables, "\n\n".join(t.to_csv(index=False) for t in tables)


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
        text, source = "\n\n".join(t.to_csv(index=False) for t in tables), "demo"
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
