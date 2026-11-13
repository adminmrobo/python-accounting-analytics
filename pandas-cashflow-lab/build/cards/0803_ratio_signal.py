from lib import *

CARD = dict(
    id="ratio_signal", ch="8. 주요 재무비율", cmd='np.where(방향 == "이상", 값 >= 기준, 값 <= 기준)', chain=True,
    title="기준과 비교해 양호·주의를 붙이고 막대로 본다", excel="IF 로 판정 열 + 조건부 서식",
    desc="비율은 숫자만 보면 좋은지 나쁜지 알기 어렵다. 비율마다 참고 기준을 하나 두고, 높을수록 좋은 비율은 '이상', 낮을수록 좋은 비율(부채비율)은 '이하' 로 판정한다. "
         "np.where 를 두 번 겹쳐 쓰면 엑셀의 IF 안에 IF 를 넣은 것과 같다. 기준은 교육용 어림값이다. 업종마다 다르므로 보고서에서는 '참고 기준' 이라고 밝힌다. "
         "% 단위인 비율만 골라 기준과 나란히 막대로 그린다.",
    code='''ratio["기준"] = [150, 200, 40, 3, 25, 5, 3, 3, 8, 6, 6, 1, 1]
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
plt.show()''',
    xl=[
        ('ratio["기준"], ratio["방향"]', "'재무비율' 시트 E열(기준)과 F열(방향, 이상/이하)을 적는다."),
        ('np.where(방향 == "이상", np.where(값 >= 기준, "양호", "주의"), np.where(값 <= 기준, "양호", "주의"))', 'G2: =IF(F2="이상", IF(C2>=E2, "양호", "주의"), IF(C2<=E2, "양호", "주의")) 를 G14 까지 채운다.'),
        ('ratio.loc[ratio["판정"] == "주의", "비율"]', "G열 필터에서 '주의' 만 체크. 홈 → 조건부 서식 → 텍스트 포함 '주의' 를 빨간색으로."),
        ('ratio[ratio["단위"] == "%"]', "D열(단위) 필터에서 % 만 고른다."),
        ("ax.barh(...) · ax.scatter(기준)", "값과 기준 두 열을 선택 → 묶은 가로 막대형. 기준 계열은 '꺾은선' 이나 '표식만' 으로 바꾼다."),
    ],
    tip="기준은 판단을 돕는 출발점일 뿐이다. 같은 업종 회사 몇 곳의 비율을 찾아 기준 열을 바꿔 보면 판정이 달라질 수 있다. 그 변화를 보고서에 적으면 좋은 분석이 된다.",
    talk=[
        dict(who="sia", text="판정. 주의 항목이 있습니다. 목록을 보세요."),
        dict(who="fly", text="기준을 누가 정했는지 보고서에 꼭 써. 업종마다 달라."),
    ],
)

def stages(ns, out):
    r = ns["ratio"]
    return [
        S("기준과 방향", "비율마다 참고 기준과 '이상/이하' 를 붙였다.", T(r[["비율", "값", "단위", "기준", "방향"]])),
        S("판정", f"주의: {', '.join(r.loc[r['판정'] == '주의', '비율']) or '없음'}.",
          T(r[["비율", "값", "기준", "판정"]], rcls=["ok" if x == "양호" else "bad" for x in r["판정"]], hl=("판정",))),
        S("막대", "% 단위 비율 여덟 개. 검은 눈금이 기준이다.", IMG("ratio_signal")),
    ]
