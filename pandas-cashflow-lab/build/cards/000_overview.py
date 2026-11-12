from lib import *
from snippets import DATA

CARD = dict(
    id="overview", ch="0. 한눈에 보는 간접법", cmd="순이익 + 조정 = 영업현금",
    title="이익에서 출발해 현금에 도착한다", excel="손익계산서 옆에 조정 열을 달아 SUM",
    desc="간접법은 손익계산서의 당기순이익에서 출발한다. 현금이 나가지 않은 비용을 더하고, 영업이 아닌 이익을 빼고, "
         "재무상태표에서 영업 관련 자산·부채가 얼마나 늘고 줄었는지를 반영하면 영업활동 현금흐름이 된다. "
         "(주)SG화학 2014년 숫자로 순이익 170 이 영업현금 270 이 되는 다섯 계단을 먼저 본다. 이 책의 나머지는 이 표를 pandas 로 만드는 과정이다.",
    code=DATA + '''

ni = pl.sum()                                   # ① 당기순이익
steps = pd.Series({
    "① 당기순이익": ni,
    "② 감가상각비 가산": -pl["감가상각비"],
    "③ 무형자산처분이익 차감": -pl["무형자산처분이익"],
    "④ 영업 관련 자산·부채 변동": 30,             # 2장에서 재무상태표로 직접 계산한다
})
print(steps)
print("⑤ 영업활동 현금흐름:", steps.sum())''',
    talk=[
        dict(who="asst", text="이익이 170 인데 현금은 왜 270 이 늘어요?"),
        dict(who="doc", text="이익과 현금은 적는 시점이 달라요. 그 차이를 계단으로 메워요."),
    ],
)

def stages(ns, out):
    pl, steps = ns["pl"], ns["steps"]
    t = steps.rename("금액").rename_axis("계단").reset_index()
    t["누계"] = t["금액"].cumsum()
    return [
        S("손익계산서", f"수익은 양수, 비용은 음수로 적었다. 모두 더하면 당기순이익 {ns['ni']}.",
          T(pl, index=True, ix_name="계정과목", hlrows=[4, 7])),
        S("네 계단", "순이익에서 시작해 감가상각비(현금이 안 나간 비용)는 더하고, 처분이익(영업이 아닌 이익)은 뺀다. 자산·부채 변동이 마지막 계단이다.",
          T(t[["계단", "금액"]], hl=("금액",))),
        S("영업현금", f"계단을 차례로 더한 누계의 끝이 영업활동 현금흐름 {steps.sum()} 이다.",
          T(t, hl=("누계",), rcls=["", "", "", "ok"]), TX(out.splitlines()[-1], "out", "출력")),
    ]
