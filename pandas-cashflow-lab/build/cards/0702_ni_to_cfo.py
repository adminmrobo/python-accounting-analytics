from lib import *

CARD = dict(
    id="ni_to_cfo", ch="7. 차트로 보기", cmd="np.cumsum → bottom", chain=True,
    title="순이익에서 영업현금까지 폭포 그리기", excel="폭포 차트",
    desc="간접법 계단을 그림으로 본다. 첫 막대는 당기순이익, 그다음 일곱 막대는 조정 항목, 마지막 막대는 영업활동 현금흐름이다. "
         "조정 막대는 직전까지의 누계에서 시작한다. np.cumsum 은 누계를 한 번에 계산하고, 그 누계를 한 칸 밀면 각 막대의 시작 높이(bottom)가 된다. "
         "늘린 막대는 초록, 줄인 막대는 빨강이다.",
    code='''op = cf[cf["활동"] == "영업활동"]
steps = op["금액"].values                      # 순이익 + 조정 일곱 개
run = np.cumsum(steps)                         # 누계
bottom = np.concatenate([[0, steps[0]], run[1:-1], [0]])     # 막대가 시작하는 높이
height = np.concatenate([[steps[0]], steps[1:], [run[-1]]])   # 막대의 길이 (마지막은 영업현금 전체)
labels = ["Net income", "Depreciation", "Disposal gain", "Receivables", "Inventory", "Prepaid", "Payables", "Wages payable", "Operating cash"]
colors = ["#1F3A5F"] + list(np.where(steps[1:] >= 0, "#2E9E5B", "#C9382A")) + ["#1F3A5F"]
print(pd.DataFrame({"bar": labels, "bottom": bottom, "height": height}))

fig, ax = plt.subplots(figsize=(7.5, 3.8))
bars = ax.bar(labels, height, bottom=bottom, color=colors)
ax.bar_label(bars, labels=list(np.char.mod("%+d", height)), fontsize=8)
ax.axhline(0, color="black", linewidth=0.8)
ax.tick_params(axis="x", labelsize=7.5, labelrotation=30)
ax.set(title=f"Net income to operating cash flow (student {sid})")
plt.show()''',
    xl=[
        ('op["금액"].values', "'현금흐름표' C2:C9 (순이익과 조정 일곱 줄)."),
        ("np.cumsum(steps)", "D2 에 =C2, D3 에 =D2+C3 을 넣고 D9 까지 채운다 (누계)."),
        ("bottom · height", "엑셀의 폭포 차트는 누계를 스스로 계산하므로 C2:C9 와 영업현금(C16)만 있으면 된다."),
        ("ax.bar(labels, height, bottom=bottom)", "C2:C9 와 C16 을 한 열로 모아 선택 → 삽입 → 차트 → 폭포. 첫 막대와 마지막 막대는 오른쪽 클릭 → '합계로 설정'."),
        ('np.where(steps[1:] >= 0, "#2E9E5B", "#C9382A")', "폭포 차트는 증가·감소 색을 자동으로 나눈다."),
    ],
    tip="빨간 막대가 길면 그 항목이 현금을 크게 묶었다는 뜻이다. 6장 why_diff 카드의 큰 세 줄과 같은 막대인지 맞춰 본다.",
    talk=[dict(who="robo", state="thinking", text="삐빅, 빨간 막대 하나가 순이익을 다 잡아먹었다.")],
)

def stages(ns, out):
    import pandas as pd
    t = pd.DataFrame({"bar": ns["labels"], "bottom": ns["bottom"].astype(int), "height": ns["height"].astype(int)})
    return [
        S("시작 높이와 길이", "누계를 한 칸 밀어 시작 높이를 만든다. 첫 막대와 마지막 막대는 0 에서 시작한다.", T(t, hl=("bottom",))),
        S("폭포", f"순이익 {ns['steps'][0]} 에서 계단을 오르내려 영업현금 {ns['run'][-1]} 에 도착한다.", IMG("ni_to_cfo")),
    ]
