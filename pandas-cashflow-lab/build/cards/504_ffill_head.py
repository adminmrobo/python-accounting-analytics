from lib import *
from snippets import RAW

CARD = dict(
    id="ffill_head", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd="where(head).ffill()",
    title="머리말 줄을 구분 열로 내려 채우기", excel="빈칸에 위 셀 값 채우기 (Ctrl+G → 빈 셀 → =위 셀)",
    desc="재무상태표에는 '자산', '부채', '자본' 이라는 머리말 줄이 있고 그 아래에 계정이 이어진다. 머리말 줄은 숫자 칸이 비어 있다. "
         "where(head) 는 머리말 줄의 이름만 남기고 나머지를 비운다. ffill 은 빈칸을 바로 위 값으로 채운다. "
         "둘을 이으면 모든 계정 옆에 자산·부채·자본 구분이 붙는다. 그다음 머리말 줄과 총계 줄을 버린다.",
    code=RAW + '''

t = raw_bs.copy()
t.columns = ["계정과목", "기말", "기초"]
t["계정과목"] = t["계정과목"].str.replace(r"\\(주석[^)]*\\)|^\\s*[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ]+\\.|\\s", "", regex=True)

head = t["기말"].isna()                            # 숫자가 없는 줄 = 머리말
t["구분"] = t["계정과목"].where(head).ffill()       # 머리말만 남기고 아래로 채운다
totals = ["자산총계", "부채총계", "자본총계", "부채와자본총계"]
t = t[~head & ~t["계정과목"].isin(totals)]          # 머리말과 총계 줄 버리기
print(t[["계정과목", "구분", "기말", "기초"]])
print(t["구분"].value_counts(sort=False).to_dict())''',
    tip="유동자산, 비유동자산 같은 중간 소계가 있는 공시는 그 이름도 totals 목록에 넣는다. 총계 줄을 버리지 않으면 자산이 두 번 더해진다.",
    talk=[
        dict(who="asst", text="구분 열이 파일에 없는데 어떻게 만들어요?"),
        dict(who="doc", text="'자산' 이라고 적힌 줄을 아래로 쭉 내려 채우면 돼요."),
    ],
)

def stages(ns, out):
    import pandas as pd
    raw = ns["raw_bs"]
    nm = raw["과 목"].str.replace(r"\(주석[^)]*\)|^\s*[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ]+\.|\s", "", regex=True)
    head = raw["당기말"].isna()
    a = pd.DataFrame({"계정과목": nm, "기말": raw["당기말"].fillna("NaN")})
    b = a.assign(구분=nm.where(head).fillna("NaN"))
    c = a.assign(구분=nm.where(head).ffill())
    g = {"자산": "g0", "부채": "g1", "자본": "g2"}
    tot = nm.isin(ns["totals"])
    return [
        S("원본", "자산 · 부채 · 자본 머리말 줄은 숫자가 NaN 이다.", T(a, rcls=["hr" if h else "" for h in head])),
        S("where(head)", "머리말 줄의 이름만 구분 열에 남는다.", T(b, hl=("구분",), rcls=["hr" if h else "" for h in head])),
        S("ffill()", "빈칸이 위 값으로 채워진다. 머리말(흐린 줄)과 총계 줄을 버리면 계정 12 줄이 남는다.",
          T(c, hl=("구분",), rcls=["dim" if (h or x) else g[k] for h, x, k in zip(head, tot, c["구분"])])),
    ]
