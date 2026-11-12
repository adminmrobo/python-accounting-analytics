from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="check", ch="4. 조립하고 검산하기", cmd='assert total.sum() == d["현금"]',
    title="세 활동의 합은 현금 증감과 같아야 한다", excel="합계 셀과 현금 증감 셀을 = 로 비교",
    desc="현금흐름표에는 정답지가 붙어 있다. 영업 + 투자 + 재무 는 재무상태표의 현금 증감과 반드시 같다. "
         "270 − 500 + 380 = 150 이고 현금은 250 에서 400 으로 150 늘었다. 이 검산을 코드에 넣어 두면 부호를 한 군데만 틀려도 바로 걸린다. "
         "일부러 매출채권의 부호를 틀리게 넣어 검산이 잡는지 본다.",
    code=CF_PARTS + '''

total = pd.Series({"영업활동": cfo.sum(), "투자활동": cfi.sum(), "재무활동": cff.sum()})
print(total)
print("세 활동 합계:", total.sum(), "| 현금 증감:", d["현금"])
assert total.sum() == d["현금"]
print("검산 통과")

# 일부러 틀려 보기: 매출채권 증가에 + 를 붙였다
bad = cfo.copy()
bad["④ 매출채권"] = 100
try:
    assert bad.sum() + cfi.sum() + cff.sum() == d["현금"], "세 활동 합계가 현금 증감과 다르다"
except AssertionError as e:
    print("검산 실패:", e, "| 차이", bad.sum() + cfi.sum() + cff.sum() - d["현금"])''',
    tip="차이가 어떤 계정 증감의 두 배이면 그 계정의 부호가 뒤집힌 것이다. 여기서는 차이 200 = 매출채권 증감 100 의 두 배다.",
    talk=[dict(who="robo", state="wrong", text="삐빅! 합계 350, 현금 증감 150. 200 이 안 맞는다.")],
)

def stages(ns, out):
    import pandas as pd
    total, d = ns["total"], ns["d"]
    lines = out.splitlines()
    ck = pd.DataFrame({"항목": ["세 활동 합계", "현금 증감 (400 − 250)"], "금액": [total.sum(), d["현금"]]})
    return [
        S("세 활동", f"{total['영업활동']} + ({total['투자활동']}) + {total['재무활동']} = {total.sum()}.",
          T(total.rename("금액"), index=True, ix_name="활동")),
        S("현금 증감과 대조", "두 숫자가 같으면 통과다.", T(ck, rcls=["ok", "ok"], hl=("금액",)), TX(lines[-2], "out", "출력")),
        S("일부러 틀리기", "매출채권 −100 을 +100 으로 바꾸면 합계가 200 커져 검산이 멈춘다.", TX(lines[-1], "err", "출력")),
    ]
