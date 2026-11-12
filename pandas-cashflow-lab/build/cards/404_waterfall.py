from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="waterfall", ch="4. 조립하고 검산하기", cmd="ax.bar(bottom=)",
    title="기초 현금에서 기말 현금까지 폭포 그리기", excel="폭포 차트",
    desc="기초 현금 250 에서 영업으로 270 이 들어오고, 투자로 500 이 나가고, 재무로 380 이 들어와 기말 400 이 된다. "
         "막대의 시작 높이(bottom)를 직전까지의 누계로 주면 막대가 계단처럼 이어진다. 차트 글자는 Colab 에서 깨지지 않게 영어로 적는다.",
    code=CF_PARTS + '''
import matplotlib.pyplot as plt

begin = 250
flow = [cfo.sum(), cfi.sum(), cff.sum()]                  # 270, -500, 380
labels = ["Opening", "Operating", "Investing", "Financing", "Closing"]
height = [begin] + flow + [begin + sum(flow)]
run = np.cumsum([begin] + flow)                           # 250, 520, 20, 400
bottom = [0, run[0], run[1], run[2], 0]
print(pd.DataFrame({"bar": labels, "bottom": bottom, "height": height}))

fig, ax = plt.subplots(figsize=(6.5, 3.5))
colors = ["#1F3A5F"] + ["#2E9E5B" if v >= 0 else "#C9382A" for v in flow] + ["#1F3A5F"]
bars = ax.bar(labels, height, bottom=bottom, color=colors)
ax.bar_label(bars, labels=[str(begin)] + [f"{v:+d}" for v in flow] + [str(height[-1])])
ax.axhline(0, color="black", linewidth=0.8)
ax.margins(y=0.15)
ax.set(title="SG Chemical 2014 cash bridge (KRW)")
plt.show()''',
    talk=[dict(who="fly", text="투자 막대가 520 에서 20 까지 내려와. 현금이 거의 바닥났던 거야.")],
)

def stages(ns, out):
    import pandas as pd
    tb = pd.DataFrame({"bar": ns["labels"], "bottom": [int(x) for x in ns["bottom"]], "height": [int(x) for x in ns["height"]]})
    return [
        S("bottom 과 height", "막대마다 시작 높이와 길이다. 투자 막대는 520 에서 시작해 −500 만큼 내려간다.", T(tb, hl=("bottom",))),
        S("폭포", "250 → +270 → −500 → +380 → 400 이 한 줄로 이어진다.", IMG("waterfall")),
    ]
