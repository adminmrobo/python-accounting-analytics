from lib import *
from snippets import DATA_D

CARD = dict(
    id="dividend", ch="3. 투자·재무활동", cmd="기초 + 순이익 − 기말",
    title="이익잉여금에서 배당금을 거꾸로 구한다", excel="기초 이익잉여금 + 당기순이익 − 기말 이익잉여금",
    desc="이익잉여금은 순이익만큼 늘고 배당만큼 준다. 기초 440 에 순이익 170 을 더하면 610 이어야 하는데 기말은 560 이다. "
         "모자란 50 이 주주에게 나간 배당금이다. 손익계산서와 재무상태표를 함께 써야 나오는 숫자다. "
         "자본금은 1,000 으로 변화가 없어 유상증자는 없다.",
    code=DATA_D + '''

re = bs.set_index("계정과목").loc["이익잉여금"]
ni = pl.sum()
dividend = re["기초"] + ni - re["기말"]
print("기초", re["기초"], "+ 순이익", ni, "- 기말", re["기말"], "=", dividend)
print("배당금의 지급:", -dividend)
print("자본금 증감:", d["자본금"])''',
    talk=[
        dict(who="asst", text="배당금은 손익계산서에 없는데 어떻게 알아요?"),
        dict(who="doc", text="이익잉여금이 덜 늘어난 만큼이에요. 거꾸로 계산해 볼까요?"),
    ],
)

def stages(ns, out):
    import pandas as pd
    re, ni, dv = ns["re"], ns["ni"], ns["dividend"]
    s = pd.DataFrame({"항목": ["기초 이익잉여금", "+ 당기순이익", "= 배당 전 금액", "기말 이익잉여금", "차이 = 배당금"],
                      "금액": [re["기초"], ni, re["기초"] + ni, re["기말"], dv]})
    return [
        S("이익잉여금", "기초 440, 기말 560. 120 만 늘었다.",
          T(ns["bs"][ns["bs"]["계정과목"] == "이익잉여금"][["계정과목", "기초", "기말", "증감"]])),
        S("거꾸로 계산", f"순이익 {ni} 이 다 쌓였다면 {re['기초'] + ni}. 실제 기말은 {re['기말']}. 차이 {dv} 이 배당금이다.",
          T(s, rcls=["", "", "hr", "", "bad"], hl=("금액",))),
    ]
