from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="check", ch="4. 조립하고 검산하기", cmd='total.sum() == d["현금"]',
    title="세 활동의 합은 현금 증감과 같아야 한다", excel='=IF(합계셀=현금증감셀, "통과", "실패")',
    desc="현금흐름표에는 정답지가 붙어 있다. 영업 + 투자 + 재무 는 재무상태표의 현금 증감과 반드시 같다. "
         "270 − 500 + 380 = 150 이고 현금은 250 에서 400 으로 150 늘었다. 두 숫자를 == 로 비교해 True 가 나오는지 본다. "
         "일부러 매출채권의 부호를 틀리게 넣어 검산이 잡는지도 본다.",
    code=CF_PARTS + '''

total = pd.Series([cfo.sum(), cfi.sum(), cff.sum()], index=["영업활동", "투자활동", "재무활동"])
print(total)
print("세 활동 합계:", total.sum(), "| 현금 증감:", d["현금"])
print("검산 통과:", total.sum() == d["현금"])

# 일부러 틀려 보기: 매출채권 증가에 + 를 붙였다
bad = cfo.copy()
bad["④ 매출채권"] = 100
bad_total = bad.sum() + cfi.sum() + cff.sum()
print("틀린 합계:", bad_total, "| 검산 통과:", bad_total == d["현금"], "| 차이:", bad_total - d["현금"])''',
    xl=[
        ("total = pd.Series([cfo.sum(), cfi.sum(), cff.sum()], ...)", "현금흐름표의 소계 세 칸: C6(영업), C9(투자), C12(재무)."),
        ("total.sum()", "C13 에 =C6+C9+C12 → 150 (현금의 증가)"),
        ('total.sum() == d["현금"]', 'C16 에 =IF(C15=재무상태표!D2, "통과", "실패"). C15 는 기초 현금 + 현금의 증가다.'),
        ('bad["④ 매출채권"] = 100', "해당 셀에 100 을 직접 덮어쓴다. 합계가 350 으로 바뀌고 검산 칸이 '실패' 로 바뀐다."),
    ],
    tip="차이가 어떤 계정 증감의 두 배이면 그 계정의 부호가 뒤집힌 것이다. 여기서는 차이 200 = 매출채권 증감 100 의 두 배다.",
    talk=[
        dict(who="sia", text="판정. 세 활동 합계 150, 현금 증감 150. 통과입니다."),
        dict(who="robo", state="wrong", text="삐빅! 부호를 틀리니 합계 350. 200 이 안 맞는다."),
    ],
)

def stages(ns, out):
    import pandas as pd
    total, d = ns["total"], ns["d"]
    lines = out.splitlines()
    ck = pd.DataFrame({"항목": ["세 활동 합계", "현금 증감 (400 − 250)"], "금액": [total.sum(), d["현금"]]})
    return [
        S("세 활동", f"{total['영업활동']} + ({total['투자활동']}) + {total['재무활동']} = {total.sum()}.",
          T(total.rename("금액"), index=True, ix_name="활동")),
        S("현금 증감과 대조", "두 숫자가 같으면 True 다.", T(ck, rcls=["ok", "ok"], hl=("금액",)), TX(lines[-2], "out", "출력")),
        S("일부러 틀리기", "매출채권 −100 을 +100 으로 바꾸면 합계가 200 커져 검산이 False 가 된다.", TX(lines[-1], "err", "출력")),
    ]
