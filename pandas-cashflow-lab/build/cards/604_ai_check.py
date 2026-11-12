from lib import *

CARD = dict(
    id="ai_check", ch="6. 생성AI 에게 맡기기", cmd="isin(허용 목록) · groupby 대차 확인",
    title="AI 의 답을 믿기 전에 세 가지를 검사한다", excel="데이터 유효성 검사",
    desc="생성AI 는 숫자를 잘못 옮기거나, 시키지 않은 분류 이름을 만들거나, 줄을 빠뜨릴 수 있다. 그래서 답을 계산에 넣기 전에 검사한다. "
         "① 분류가 허용한 이름인가(isin), ② 대차가 맞는가(groupby), ③ 숫자 열이 정말 숫자인가. "
         "아래는 일부러 틀리게 만든 답이다. 매출채권 기말 330 을 3300 으로 읽었고, 분류에 '운전자본' 이라는 없는 이름을 썼다. 검사가 둘 다 잡아낸다.",
    code='''import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# 틀린 답의 예 (재무상태표 일부만 보인다)
bs = pd.DataFrame({
    "계정과목": ["현금및현금성자산", "매출채권", "상품재고", "매입채무", "자본금"],
    "구분": ["자산", "자산", "자산", "부채", "자본"],
    "기초": [250, 230, 280, 100, 660],
    "기말": [400, 3300, 220, 140, 810],          # 매출채권 330 → 3300 으로 잘못 읽음
    "분류": ["현금", "운전자본", "영업", "영업", "재무"],
})
BS_KINDS = ["현금", "영업", "투자", "비현금", "재무", "이익잉여금", "미분류"]

problems = []
bad_kind = bs[~bs["분류"].isin(BS_KINDS)]
if len(bad_kind):
    problems.append("없는 분류 이름: " + ", ".join(bad_kind["계정과목"] + "=" + bad_kind["분류"]))
side = bs.groupby("구분")[["기초", "기말"]].sum()
gap = side.loc["자산"] - side.drop("자산").sum()
if (gap != 0).any():
    problems.append(f"대차 불일치: 기초 {gap['기초']}, 기말 {gap['기말']}")
if not all(pd.api.types.is_integer_dtype(bs[c]) for c in ["기초", "기말"]):
    problems.append("숫자가 아닌 값이 있다")
print(side)
for p in problems:
    print("문제:", p)''',
    tip="대차 차이 2970 = 3300 − 330 이다. 차이 금액이 어떤 숫자의 9 배, 90 배이면 자릿수를 잘못 읽었을 가능성이 높다. 문제가 있으면 앱에서는 사람이 표를 직접 고치게 한다.",
    talk=[
        dict(who="robo", state="success", text="삐빅! AI 가 표를 다 읽었다. 바로 계산한다!"),
        dict(who="fly", text="잠깐. 기말 자산이 3920 인데 부채와 자본은 950 이야."),
    ],
)

def stages(ns, out):
    bs, side = ns["bs"], ns["side"]
    return [
        S("AI 의 답", "얼핏 보면 멀쩡한 표다.", T(bs)),
        S("검사 ① 분류 이름", "허용 목록에 없는 '운전자본' 이 걸린다.",
          T(bs, cls={(1, "분류"): "bad"}, rcls=["", "bad", "", "", ""])),
        S("검사 ② 대차", f"기말 자산 {side.loc['자산', '기말']} 과 부채 + 자본 {side.drop('자산')['기말'].sum()} 이 다르다. 기초는 맞으니 기말 숫자 중 하나가 틀렸다.",
          T(side, index=True), TX("\n".join(l for l in out.splitlines() if l.startswith("문제")), "err", "출력")),
    ]
