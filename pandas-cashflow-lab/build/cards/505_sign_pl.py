from lib import *
from snippets import RAW, TOOLS

CARD = dict(
    id="sign_pl", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd='금액.where(수익인가, -금액)',
    title="손익계산서: 소계를 버리고 비용에 − 를 붙인다", excel="소계 행 삭제, 비용 행에 −1 곱하기",
    desc="공시의 손익계산서는 비용도 양수로 적고, 매출총이익·영업이익·당기순이익 같은 소계가 중간에 끼어 있다. "
         "소계 줄은 isin 으로 골라 버린다. 남은 줄에서 이름에 매출액·수익·이익이 들어가면 수익, 아니면 비용으로 보고 비용에만 − 를 붙인다. "
         "where(조건, 다른 값) 은 조건이 참인 줄은 그대로 두고 거짓인 줄만 다른 값으로 바꾼다. 다 더한 값이 원본의 당기순이익 170 과 같은지 확인한다.",
    code=RAW + "\n" + TOOLS.split("RULE_BS")[0].replace("import pandas as pd\n", "") + "\n" + TOOLS[TOOLS.index("def clean_name"):TOOLS.index("def by_rule")] + '''
t = raw_pl.copy()
t.columns = ["계정과목", "금액"]
t["계정과목"] = t["계정과목"].map(clean_name)
stated_ni = to_num(t.loc[t["계정과목"] == "당기순이익", "금액"].item())   # 원본에 적힌 순이익

t = t[~t["계정과목"].isin(SUBTOTAL)].copy()                 # 소계 줄 버리기
t["금액"] = t["금액"].map(to_num)
plus = t["계정과목"].str.contains("매출액|수익|이익")          # 수익인가
t["금액"] = t["금액"].where(plus, -t["금액"])                # 비용에만 − 를 붙인다
print(t)
print("합계:", t["금액"].sum(), "| 원본의 당기순이익:", stated_ni)
assert t["금액"].sum() == stated_ni''',
    tip='"매출원가" 에는 매출이라는 글자가 있어서, 수익 낱말을 "매출" 로 쓰면 원가가 수익으로 분류된다. 그래서 "매출액" 으로 적었다. 내 회사의 계정 이름으로 plus 를 꼭 출력해 확인한다.',
    talk=[dict(who="fly", text="영업이익 줄을 안 버리면 이익을 두 번 더하게 돼.")],
)

def stages(ns, out):
    import pandas as pd
    raw, t = ns["raw_pl"], ns["t"]
    nm = raw["과 목"].map(ns["clean_name"])
    sub = nm.isin(ns["SUBTOTAL"])
    a = pd.DataFrame({"계정과목": nm, "당기": raw["당기"]})
    return [
        S("원본", "소계 여섯 줄(노랑)이 섞여 있고 비용도 양수다.", T(a, rcls=["hr" if s else "" for s in sub])),
        S("소계 버리기", "계정 여덟 줄만 남는다.", T(a[~sub])),
        S("부호 붙이기", f"수익 두 줄(초록)은 그대로, 비용 여섯 줄(빨강)은 음수. 합계 {t['금액'].sum()} 이 원본의 당기순이익과 같다.",
          T(t, rcls=["ok" if p else "bad" for p in ns["plus"]], hl=("금액",))),
    ]
