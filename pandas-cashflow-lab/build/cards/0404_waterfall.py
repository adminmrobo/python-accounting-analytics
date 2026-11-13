from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="waterfall", ch="4. 조립하고 검산하기", cmd="ax.bar(bottom=)",
    title="기초 현금에서 기말 현금까지 폭포 그리기", excel="삽입 → 차트 → 폭포",
    desc="기초 현금 250 에서 영업으로 270 이 들어오고, 투자로 500 이 나가고, 재무로 380 이 들어와 기말 400 이 된다. "
         "막대의 시작 높이(bottom)를 직전까지의 누계로 주면 막대가 계단처럼 이어진다. 차트 글자는 Colab 에서 깨지지 않게 영어로 적는다.",
    code=CF_PARTS + '''
import matplotlib.pyplot as plt

begin = 250
a = cfo.sum()                                  # 270
b = cfi.sum()                                  # -500
c = cff.sum()                                  # 380
labels = ["Opening", "Operating", "Investing", "Financing", "Closing"]
height = [begin, a, b, c, begin + a + b + c]
bottom = [0, begin, begin + a, begin + a + b, 0]          # 막대가 시작하는 높이 = 직전까지의 누계
table = pd.DataFrame()
table["bar"] = labels
table["bottom"] = bottom
table["height"] = height
print(table)

fig, ax = plt.subplots(figsize=(6.5, 3.5))
colors = ["#1F3A5F", "#2E9E5B", "#C9382A", "#2E9E5B", "#1F3A5F"]
bars = ax.bar(labels, height, bottom=bottom, color=colors)
ax.bar_label(bars, labels=["250", "+270", "-500", "+380", "400"])
ax.axhline(0, color="black", linewidth=0.8)
ax.margins(y=0.15)
ax.set(title="SG Chemical 2014 cash bridge (KRW)")
plt.show()''',
    xl=[
        ("height = [begin, a, b, c, begin + a + b + c]", "한 열에 250, 270, −500, 380, 400 을 적는다. 옆 열에 이름(기초, 영업, 투자, 재무, 기말)을 적는다."),
        ("bottom = [0, begin, begin + a, ...]", "엑셀의 폭포 차트는 시작 높이를 스스로 계산한다. 직접 그리려면 누계 열 =SUM($B$2:B2) 를 만든다."),
        ("ax.bar(labels, height, bottom=bottom)", "두 열을 선택하고 삽입 → 차트 → 폭포. 기초와 기말 막대는 마우스 오른쪽 → '합계로 설정'."),
        ("ax.bar_label(...)", "차트 요소 → 데이터 레이블"),
    ],
    talk=[dict(who="fly", text="투자 막대가 520 에서 20 까지 내려와. 현금이 거의 바닥났던 거야.")],
)

def stages(ns, out):
    tb = ns["table"]
    return [
        S("bottom 과 height", "막대마다 시작 높이와 길이다. 투자 막대는 520 에서 시작해 −500 만큼 내려간다.", T(tb, hl=("bottom",))),
        S("폭포", "250 → +270 → −500 → +380 → 400 이 한 줄로 이어진다.", IMG("waterfall")),
    ]
