from lib import *

CARD = dict(
    id="ratio_parts", ch="8. 주요 재무비율", cmd="합계 · 평균 · 이익 단계", chain=True,
    title="비율에 들어갈 재료를 먼저 모은다", excel="SUMIFS 와 평균 셀",
    desc="재무비율은 '재료 ÷ 재료' 다. 재료를 먼저 이름 붙여 모아 두면 비율 식이 말과 같은 모양이 된다. "
         "재무상태표에서는 유동자산·유동부채·총자산·부채·자본의 합계를, 손익계산서에서는 매출총이익·영업이익·이자비용을 만든다. "
         "회전율과 ROA·ROE 는 1년 동안의 흐름(손익)을 한 시점의 잔액으로 나누므로, 기초와 기말의 평균 잔액을 쓴다.",
    code='''cur_assets = bs.loc[(bs["구분"] == "자산") & (bs["세부"] == "유동"), "기말"].sum()
cur_liab = bs.loc[(bs["구분"] == "부채") & (bs["세부"] == "유동"), "기말"].sum()
assets0 = bs.loc[bs["구분"] == "자산", "기초"].sum()
assets1 = bs.loc[bs["구분"] == "자산", "기말"].sum()
liab1 = bs.loc[bs["구분"] == "부채", "기말"].sum()
equity0 = bs.loc[bs["구분"] == "자본", "기초"].sum()
equity1 = bs.loc[bs["구분"] == "자본", "기말"].sum()

sales = pl["매출액"]
cogs = -pl["매출원가"]                                    # 비용은 음수로 들어 있어 − 를 붙여 양수로
gross = sales - cogs                                      # 매출총이익
op_income = gross + pl["보험료"] + pl["급여"] + pl["감가상각비"] + pl["기타영업비용"]   # 영업이익
interest = -pl["이자비용"]
avg_assets = (assets0 + assets1) / 2
avg_equity = (equity0 + equity1) / 2
avg_ar = (b.loc["매출채권", "기초"] + b.loc["매출채권", "기말"]) / 2
avg_inv = (b.loc["상품재고", "기초"] + b.loc["상품재고", "기말"]) / 2

parts = pd.Series([cur_assets, cur_liab, assets1, liab1, equity1, sales, gross, op_income, interest, ni, avg_assets, avg_equity, avg_ar, avg_inv, cfo],
index=["유동자산", "유동부채", "총자산(기말)", "부채(기말)", "자본(기말)", "매출액", "매출총이익", "영업이익", "이자비용", "당기순이익",
"평균총자산", "평균자본", "평균매출채권", "평균재고", "영업활동현금흐름"])
print(parts)''',
    xl=[
        ('bs.loc[(bs["구분"] == "자산") & (bs["세부"] == "유동"), "기말"].sum()', '=SUMIFS(H2:H13, D2:D13, "자산", E2:E13, "유동")'),
        ('bs.loc[bs["구분"] == "자산", "기초"].sum()', '=SUMIF(D2:D13, "자산", G2:G13)'),
        ("gross = sales - cogs", "=H14-H15"),
        ("op_income = gross + 보험료 + 급여 + 감가상각비 + 기타영업비용 (음수)", '=SUMIF(E14:E21, "영업", J14:J21). J열은 부호를 붙인 금액.'),
        ("avg_assets = (assets0 + assets1) / 2", "=(기초 자산 합계 + 기말 자산 합계)/2"),
        ('avg_ar = (b.loc["매출채권", "기초"] + b.loc["매출채권", "기말"]) / 2', "=AVERAGE(G3:H3)"),
        ("cfo", "'현금흐름표' C16"),
    ],
    tip="& 는 '그리고' 다. 조건 두 개를 & 로 이을 때는 조건마다 괄호를 친다. 엑셀의 SUMIFS 에 조건을 두 개 넣는 것과 같다.",
)

def stages(ns, out):
    p = ns["parts"]
    return [
        S("재무상태표 재료", "합계 다섯 개.", T(p.iloc[:5].rename("금액"), index=True, ix_name="재료", rcls=["g0", "g1", "g0", "g1", "g2"])),
        S("손익 재료", "매출액에서 단계별 이익까지.", T(p.iloc[5:10].rename("금액"), index=True, ix_name="재료", rcls=["", "g2", "g2", "bad", "ok"])),
        S("평균과 현금", "회전율·ROA·ROE 에 쓰는 평균 잔액과 영업현금.", T(p.iloc[10:].round(1).rename("금액"), index=True, ix_name="재료")),
    ]
