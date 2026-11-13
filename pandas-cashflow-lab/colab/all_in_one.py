# pandas 로 만드는 현금흐름표 · 한 셀로 끝내기
# Colab 새 노트북의 첫 셀에 통째로 붙여 넣고 Shift+Enter → 생성기에서 받은 재무제표_학번.csv 를 고른다.

# ── 5장 · 학번으로 만든 CSV 를 Colab 에 올려 읽는다 ──
import numpy as np
import pandas as pd
from google.colab import files
pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄 맞춤

up = files.upload()                  # '파일 선택' 단추를 눌러 재무제표_학번.csv 를 고른다
name = list(up)[0]                   # 올린 파일 이름
fs = pd.read_csv(name)               # CSV → 표
company = fs["회사명"].iloc[0]
sid = str(fs["학번"].iloc[0])
print("회사:", company, "| 학번:", sid, "| 줄 수:", len(fs))
print(fs[["표", "구분", "세부", "계정과목", "기초", "기말"]])

# ── 5장 · 한 파일을 재무상태표와 손익계산서로 나눈다 ──
bs = fs[fs["표"] == "재무상태표"].copy()
bs["기초"] = bs["기초"].astype(int)            # 손익 줄의 빈칸 때문에 실수로 읽힌 것을 정수로
bs["증감"] = bs["기말"] - bs["기초"]
b = bs.set_index("계정과목")                    # b.loc["현금", "기말"] 처럼 꺼내 쓴다
d = b["증감"]                                  # d["매출채권"] 처럼 꺼내 쓴다
print(bs[["계정과목", "구분", "세부", "기초", "기말", "증감"]])

p = fs[fs["표"] == "손익계산서"]
pl = pd.Series(np.where(p["구분"] == "수익", p["기말"], -p["기말"]), index=p["계정과목"].values, name="금액")
ni = pl.sum()                                  # 당기순이익
print(pl)
print("당기순이익:", ni)

# ── 5장 · 대차는 맞는데, 이익과 현금이 안 맞는다 ──
side = bs.groupby("구분")[["기초", "기말"]].sum()
gap = side.loc["자산"] - side.loc["부채"] - side.loc["자본"]
print(side)
print("대차가 맞는가:", gap.abs().sum() == 0)

print("당기순이익:", ni)
print("현금의 증감:", d["현금"], "(", b.loc["현금", "기초"], "→", b.loc["현금", "기말"], ")")
print("차이 (현금 증감 - 순이익):", d["현금"] - ni)

# ── 6장 · 2~4장의 식을 그대로 써서 내 회사의 현금흐름표를 만든다 ──
ops = ["매출채권", "상품재고", "선급보험료", "매입채무", "미지급급여"]
wc = b.loc[ops]
wc_effect = np.where(wc["구분"] == "자산", -wc["증감"], wc["증감"])     # 자산 증가는 −, 부채 증가는 +
gain = pl["무형자산처분이익"]
dividend = b.loc["이익잉여금", "기초"] + ni - b.loc["이익잉여금", "기말"]

cf = pd.DataFrame()
cf["활동"] = ["영업활동"] * 8 + ["투자활동"] * 2 + ["재무활동"] * 3
cf["항목"] = ["① 당기순이익", "② 감가상각비 가산", "③ 무형자산처분이익 차감", "④ 매출채권 증감", "④ 상품재고 증감",
"④ 선급보험료 증감", "④ 매입채무 증감", "④ 미지급급여 증감", "유형자산의 취득", "무형자산의 처분",
"차입금의 순증감", "유상증자", "배당금의 지급"]
cf["금액"] = [ni, -pl["감가상각비"], -gain] + list(wc_effect) + [-d["유형자산"], -d["무형자산"] + gain, d["차입금"], d["자본금"], -dividend]
cf["금액"] = cf["금액"].astype(int)
print(cf)
total = cf.groupby("활동", sort=False)["금액"].sum()
print(total)

# ── 6장 · 검산하고, 이익과 현금이 다른 이유 세 가지를 찾는다 ──
print("세 활동 합계:", total.sum(), "| 현금 증감:", d["현금"], "| 검산 통과:", total.sum() == d["현금"])
cfo = total["영업활동"]
print("당기순이익:", ni, "→ 영업활동 현금흐름:", cfo, "| 차이:", cfo - ni)

adj = cf[cf["항목"].str[0].isin(["②", "③", "④"])].copy()    # 조정 항목만
adj["크기"] = adj["금액"].abs()
top3 = adj.sort_values("크기", ascending=False).head(3)
print(top3[["항목", "금액"]])

# ── 7장 · 재무상태표의 구조를 쌓은 막대로 ──
import matplotlib.pyplot as plt

sumif = bs.groupby(["구분", "세부"])[["기초", "기말"]].sum()     # 구분·세부별 합계
print(sumif)
ca = sumif.loc[("자산", "유동")]
nca = sumif.loc[("자산", "비유동")]
cl = sumif.loc[("부채", "유동")]
ncl = sumif.loc[("부채", "비유동")]
eq = sumif.loc[("자본", "자본")]

x = ["Assets\n(open)", "L+E\n(open)", "Assets\n(close)", "L+E\n(close)"]
lower = [ca["기초"], cl["기초"], ca["기말"], cl["기말"]]           # 아래 칸: 유동자산 / 유동부채
middle = [nca["기초"], ncl["기초"], nca["기말"], ncl["기말"]]      # 가운데 칸: 비유동자산 / 비유동부채
upper = [0, eq["기초"], 0, eq["기말"]]                              # 위 칸: 자본

fig, ax = plt.subplots(figsize=(6.5, 3.8))
ax.bar(x, lower, color="#4472C4", label="Current")
ax.bar(x, middle, bottom=lower, color="#A9BEE3", label="Non-current")
ax.bar(x, upper, bottom=np.add(lower, middle), color="#2E9E5B", label="Equity")
ax.legend(loc="upper left", fontsize=8)
ax.set(title=f"Balance sheet structure (student {sid}, KRW mn)")
plt.show()

# ── 7장 · 순이익에서 영업현금까지 폭포 그리기 ──
op = cf[cf["활동"] == "영업활동"]
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
plt.show()

# ── 7장 · 기초 현금에서 기말 현금까지 다리 놓기 ──
cash0 = b.loc["현금", "기초"]
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
plt.show()

# ── 8장 · 비율에 들어갈 재료를 먼저 모은다 ──
cur_assets = bs.loc[(bs["구분"] == "자산") & (bs["세부"] == "유동"), "기말"].sum()
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
print(parts)

# ── 8장 · 주요 재무비율 열세 개를 한 표로 ──
ratio = pd.DataFrame()
ratio["분류"] = ["안정성"] * 4 + ["수익성"] * 5 + ["활동성"] * 3 + ["현금흐름"]
ratio["비율"] = ["유동비율", "부채비율", "자기자본비율", "이자보상배율", "매출총이익률", "영업이익률", "순이익률", "ROA", "ROE",
"매출채권회전율", "재고자산회전율", "총자산회전율", "영업현금흐름/순이익"]
ratio["값"] = [cur_assets / cur_liab * 100, liab1 / equity1 * 100, equity1 / assets1 * 100, op_income / interest,
gross / sales * 100, op_income / sales * 100, ni / sales * 100, ni / avg_assets * 100, ni / avg_equity * 100,
sales / avg_ar, cogs / avg_inv, sales / avg_assets, cfo / ni]
ratio["값"] = ratio["값"].round(1)
ratio["단위"] = ["%", "%", "%", "배", "%", "%", "%", "%", "%", "회", "회", "회", "배"]
ratio["계산식"] = ["유동자산 ÷ 유동부채", "부채 ÷ 자본", "자본 ÷ 총자산", "영업이익 ÷ 이자비용", "매출총이익 ÷ 매출액", "영업이익 ÷ 매출액",
"당기순이익 ÷ 매출액", "당기순이익 ÷ 평균총자산", "당기순이익 ÷ 평균자본", "매출액 ÷ 평균매출채권", "매출원가 ÷ 평균재고",
"매출액 ÷ 평균총자산", "영업활동현금흐름 ÷ 당기순이익"]
print(ratio)

# ── 8장 · 기준과 비교해 양호·주의를 붙이고 막대로 본다 ──
ratio["기준"] = [150, 200, 40, 3, 25, 5, 3, 3, 8, 6, 6, 1, 1]
ratio["방향"] = ["이상", "이하", "이상", "이상", "이상", "이상", "이상", "이상", "이상", "이상", "이상", "이상", "이상"]
ratio["판정"] = np.where(ratio["방향"] == "이상", np.where(ratio["값"] >= ratio["기준"], "양호", "주의"), np.where(ratio["값"] <= ratio["기준"], "양호", "주의"))
print(ratio[["분류", "비율", "값", "단위", "기준", "방향", "판정"]])
print("주의:", ratio.loc[ratio["판정"] == "주의", "비율"].tolist())

pct = ratio[ratio["단위"] == "%"].copy()
pct["eng"] = ["Current", "Debt/Equity", "Equity/Assets", "Gross margin", "Op. margin", "Net margin", "ROA", "ROE"]
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.barh(pct["eng"], pct["값"], color=np.where(pct["판정"] == "양호", "#2E9E5B", "#C9382A"))
ax.scatter(pct["기준"], pct["eng"], color="black", marker="|", s=300, label="Reference")
ax.invert_yaxis()
ax.legend(loc="lower right", fontsize=8)
ax.set(title=f"Ratios in % vs reference (student {sid})", xlabel="%")
plt.show()

# ── 9장 · 현금흐름표와 재무비율을 CSV 로 저장해 내려받는다 ──
cf_name = f"현금흐름표_{sid}.csv"
ratio_name = f"재무비율_{sid}.csv"
cf.to_csv(cf_name, index=False, encoding="utf-8-sig")
ratio.to_csv(ratio_name, index=False, encoding="utf-8-sig")
files.download(cf_name)
files.download(ratio_name)

check_cf = pd.read_csv(cf_name)                     # 다시 읽어 확인
print(cf_name, "→", len(check_cf), "줄, 합계", check_cf["금액"].sum(), "(현금 증감", d["현금"], ")")
print(ratio_name, "→", len(pd.read_csv(ratio_name)), "줄")

# ── 9장 · 차트 네 장을 한 그림으로 모아 저장한다 ──
fig, axes = plt.subplots(2, 2, figsize=(11, 7))
axes[0, 0].bar(x, lower, color="#4472C4")
axes[0, 0].bar(x, middle, bottom=lower, color="#A9BEE3")
axes[0, 0].bar(x, upper, bottom=np.add(lower, middle), color="#2E9E5B")
axes[0, 0].set(title="Balance sheet structure")
axes[0, 1].bar(b_labels, b_height, bottom=b_bottom, color=b_colors)
axes[0, 1].axhline(0, color="black", linewidth=0.8)
axes[0, 1].set(title="Cash bridge")
op_labels = ["NI", "Dep", "Gain", "AR", "Inv", "Pre", "AP", "Wage", "CFO"]
op_height = np.concatenate([[steps[0]], steps[1:], [run[-1]]])
op_bottom = np.concatenate([[0, steps[0]], run[1:-1], [0]])
op_colors = ["#1F3A5F"] + list(np.where(steps[1:] >= 0, "#2E9E5B", "#C9382A")) + ["#1F3A5F"]
axes[1, 0].bar(op_labels, op_height, bottom=op_bottom, color=op_colors)
axes[1, 0].axhline(0, color="black", linewidth=0.8)
axes[1, 0].set(title="Net income to operating cash")
axes[1, 1].barh(pct["eng"], pct["값"], color=np.where(pct["판정"] == "양호", "#2E9E5B", "#C9382A"))
axes[1, 1].scatter(pct["기준"], pct["eng"], color="black", marker="|", s=200)
axes[1, 1].invert_yaxis()
axes[1, 1].set(title="Ratios in % vs reference")
fig.suptitle(f"Student {sid} (KRW mn)")
fig.tight_layout()
png_name = f"차트_{sid}.png"
fig.savefig(png_name, dpi=150)
files.download(png_name)
plt.show()
print("저장:", png_name)

# ── 10장 · 정해진 프롬프트에 내 숫자를 붙여 한 덩어리로 출력한다 ──
REPORT = """너는 기업 재무분석가다. 아래 [자료]는 학번으로 만든 가상 회사의 재무제표와, 그것으로 파이썬(pandas)이 계산한 간접법 현금흐름표와 재무비율이다.
이 자료만 써서 한국어 분석보고서를 써라.

[지킬 것]
1. 자료에 있는 숫자만 쓴다. 새 숫자를 지어내지 않는다. 계산이 필요하면 식과 함께 보인다.
2. 단위는 백만원. 비율은 자료의 단위(%, 회, 배)를 그대로 쓴다.
3. 판정의 '기준' 은 교육용 참고값이라고 밝힌다. 업종 평균이라고 쓰지 않는다.
4. 투자 권유나 주가 전망은 쓰지 않는다.
5. 표가 필요하면 마크다운 표로 쓴다. 전체 분량은 A4 두 쪽 안팎.

[보고서 구성]
1. 한 줄 요약
2. 회사 개요: 매출액, 총자산, 당기순이익, 영업활동 현금흐름
3. 이익과 현금은 왜 다른가: 당기순이익과 영업활동 현금흐름의 차이를, 간접법 조정 항목 중 금액이 큰 세 개로 설명
4. 현금흐름의 모양: 영업·투자·재무 세 활동의 부호 조합으로 본 회사의 상황, 차입·유상증자·배당의 역할
5. 수익성: 매출총이익률, 영업이익률, 순이익률, ROA, ROE
6. 안정성: 유동비율, 부채비율, 자기자본비율, 이자보상배율
7. 활동성: 매출채권회전율, 재고자산회전율, 총자산회전율
8. 위험 신호와, 경영진에게 묻고 싶은 질문 세 가지
9. 종합 의견과 이 분석의 한계 (1년치 자료, 가상 회사, 주석 없음, 참고 기준의 한계)

[자료]
"""

info = f"회사명: {company} (학번 {sid} 로 만든 가상 회사), 단위: 백만원, 회계기간: 1년\n"
statements = fs[["표", "구분", "세부", "계정과목", "기초", "기말"]].to_csv(index=False)
cf_text = cf.to_csv(index=False)
ratio_text = ratio[["분류", "비율", "값", "단위", "계산식", "기준", "방향", "판정"]].to_csv(index=False)
prompt = REPORT + "[회사]\n" + info + "\n[재무제표]\n" + statements + "\n[현금흐름표 (간접법)]\n" + cf_text + "\n[재무비율]\n" + ratio_text
print(prompt)                                          # ← 이 출력 전체를 복사해 생성AI 에 붙여 넣는다

prompt_name = f"보고서프롬프트_{sid}.txt"
f = open(prompt_name, "w", encoding="utf-8")
f.write(prompt)
f.close()
files.download(prompt_name)

# ── 10장 · 생성AI 의 보고서를 정답표로 검산한다 ──
key = pd.DataFrame()
key["항목"] = ["당기순이익", "영업활동 현금흐름", "투자활동 현금흐름", "재무활동 현금흐름", "현금의 증감",
"이익과 현금의 차이 1위 항목", "부채비율(%)", "영업이익률(%)", "ROE(%)", "주의 판정 비율"]
key["정답"] = [ni, total["영업활동"], total["투자활동"], total["재무활동"], d["현금"],
top3["항목"].iloc[0] + " " + str(top3["금액"].iloc[0]), ratio.loc[1, "값"], ratio.loc[5, "값"], ratio.loc[8, "값"],
", ".join(ratio.loc[ratio["판정"] == "주의", "비율"])]
key["보고서의 숫자"] = ""
key["같은가 (O/X)"] = ""
print(key)

key_name = f"보고서검증_{sid}.csv"
key.to_csv(key_name, index=False, encoding="utf-8-sig")
files.download(key_name)
