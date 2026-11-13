from lib import *

CARD = dict(
    id="bs_chart", ch="7. 차트로 보기", cmd="ax.bar(bottom=) 쌓기", chain=True,
    title="재무상태표의 구조를 쌓은 막대로", excel="누적 세로 막대형 차트",
    desc="기초와 기말에 자산 막대와 부채+자본 막대를 하나씩 세운다. 자산 막대는 유동·비유동, 부채+자본 막대는 유동부채·비유동부채·자본으로 쌓는다. "
         "두 막대의 높이가 같으면 대차가 맞는 것이다. 막대를 쌓을 때는 bottom 에 아래 칸의 높이를 준다. 차트 글자는 Colab 에서 깨지지 않게 영어로 적는다.",
    code='''import matplotlib.pyplot as plt

sumif = bs.groupby(["구분", "세부"])[["기초", "기말"]].sum()     # 구분·세부별 합계
print(sumif)
ca = sumif.loc[("자산", "유동")]
nca = sumif.loc[("자산", "비유동")]
cl = sumif.loc[("부채", "유동")]
ncl = sumif.loc[("부채", "비유동")]
eq = sumif.loc[("자본", "자본")]

x = ["Assets\\n(open)", "L+E\\n(open)", "Assets\\n(close)", "L+E\\n(close)"]
lower = [ca["기초"], cl["기초"], ca["기말"], cl["기말"]]           # 아래 칸: 유동자산 / 유동부채
middle = [nca["기초"], ncl["기초"], nca["기말"], ncl["기말"]]      # 가운데 칸: 비유동자산 / 비유동부채
upper = [0, eq["기초"], 0, eq["기말"]]                              # 위 칸: 자본

fig, ax = plt.subplots(figsize=(6.5, 3.8))
ax.bar(x, lower, color="#4472C4", label="Current")
ax.bar(x, middle, bottom=lower, color="#A9BEE3", label="Non-current")
ax.bar(x, upper, bottom=np.add(lower, middle), color="#2E9E5B", label="Equity")
ax.legend(loc="upper left", fontsize=8)
ax.set(title=f"Balance sheet structure (student {sid}, KRW mn)")
plt.show()''',
    xl=[
        ('bs.groupby(["구분", "세부"])[["기초", "기말"]].sum()', '피벗 테이블: 행 = 구분, 세부 / 값 = 기초 합계, 기말 합계. 또는 =SUMIFS(G:G, D:D, "자산", E:E, "유동").'),
        ("x, lower, middle, upper", "네 열(자산 기초, 부채+자본 기초, 자산 기말, 부채+자본 기말)과 세 행(유동, 비유동, 자본)짜리 작은 표를 만든다."),
        ("ax.bar(..., bottom=lower) 세 번", "그 표를 선택하고 삽입 → 차트 → 누적 세로 막대형."),
        ("ax.legend · ax.set(title=...)", "차트 요소 → 범례, 차트 제목"),
    ],
    talk=[dict(who="moa", text="왼쪽 막대랑 오른쪽 막대 높이가 같아요. 대차가 맞는 거죠?")],
)

def stages(ns, out):
    import pandas as pd
    t = pd.DataFrame({"bar": [s.replace("\n", " ") for s in ns["x"]], "lower": ns["lower"], "middle": ns["middle"], "upper": ns["upper"]})
    t["top"] = t["lower"] + t["middle"] + t["upper"]
    return [
        S("쌓을 숫자", "막대마다 세 칸의 높이. 자산 막대는 위 칸(자본)이 0 이다. top 이 짝끼리 같다.", T(t, hl=("top",))),
        S("쌓은 막대", "기초와 기말 모두 두 막대의 높이가 같다.", IMG("bs_chart")),
    ]
