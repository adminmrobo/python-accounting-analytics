from lib import *

CARD = dict(
    id="cash_bridge", ch="7. 차트로 보기", cmd="기초 현금 → 세 활동 → 기말 현금", chain=True,
    title="기초 현금에서 기말 현금까지 다리 놓기", excel="폭포 차트",
    desc="4장 waterfall 카드와 같은 그림을 내 회사 숫자로 그린다. 기초 현금에서 영업·투자·재무 세 활동을 차례로 더하면 기말 현금이다. "
         "세 활동의 부호 조합(+ − + 처럼)이 회사가 지금 어떤 상황인지 보여 준다. 10장 보고서에서 이 조합을 해석한다.",
    code='''cash0 = b.loc["현금", "기초"]
cash1 = b.loc["현금", "기말"]
flow = total.values                                   # 영업, 투자, 재무
b_labels = ["Opening", "Operating", "Investing", "Financing", "Closing"]
b_height = np.concatenate([[cash0], flow, [cash1]])
b_bottom = np.concatenate([[0], cash0 + np.cumsum(flow) - flow, [0]])
b_colors = ["#1F3A5F"] + list(np.where(flow >= 0, "#2E9E5B", "#C9382A")) + ["#1F3A5F"]
print(pd.DataFrame({"bar": b_labels, "bottom": b_bottom, "height": b_height}))
print("부호 조합 (영업, 투자, 재무):", list(np.where(flow >= 0, "+", "-")))

fig, ax = plt.subplots(figsize=(6.5, 3.6))
bars = ax.bar(b_labels, b_height, bottom=b_bottom, color=b_colors)
ax.bar_label(bars, labels=[str(cash0)] + list(np.char.mod("%+d", flow)) + [str(cash1)])
ax.axhline(0, color="black", linewidth=0.8)
ax.margins(y=0.15)
ax.set(title=f"Cash bridge (student {sid}, KRW mn)")
plt.show()''',
    xl=[
        ('b.loc["현금", "기초"] · b.loc["현금", "기말"]', "재무제표!G2 · 재무제표!H2"),
        ("flow = total.values", "'현금흐름표' C16:C18"),
        ("cash0 + np.cumsum(flow) - flow", "각 활동 막대가 시작하는 높이. 폭포 차트가 스스로 계산한다."),
        ("ax.bar(...)", "G2, C16, C17, C18, H2 를 한 열로 모아 폭포 차트. 첫·마지막 막대는 '합계로 설정'."),
        ('np.where(flow >= 0, "+", "-")', '=IF(C16>=0, "+", "-") 를 세 칸에'),
    ],
    tip="흔한 부호 조합: (+ − −) 영업으로 번 돈으로 투자하고 빚을 갚는 안정기, (+ − +) 벌기도 하지만 빌려서 더 투자하는 성장기, (− − +) 영업이 현금을 못 벌어 빌려서 버티는 상태, (− + +) 자산을 팔고 빌려서 버티는 위험 신호.",
    talk=[dict(who="asst", text="영업이 플러스인데도 빌린 돈으로 투자했네요.")],
)

def stages(ns, out):
    import pandas as pd
    t = pd.DataFrame({"bar": ns["b_labels"], "bottom": ns["b_bottom"].astype(int), "height": ns["b_height"].astype(int)})
    return [
        S("다리의 칸", f"기초 {ns['cash0']} 에서 시작해 기말 {ns['cash1']} 에 도착한다. 부호 조합: {''.join(np.where(ns['flow'] >= 0, '+', '−'))}.", T(t, hl=("bottom",))),
        S("다리", "세 활동이 현금을 어떻게 움직였는지 한눈에 본다.", IMG("cash_bridge")),
    ]
