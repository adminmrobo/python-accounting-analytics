from lib import *
from snippets import DATA_D

CARD = dict(
    id="intangible", ch="3. 투자·재무활동", cmd='-d["무형자산"] + pl["무형자산처분이익"]',
    title="판 자산의 장부금액에 처분이익을 더한다", excel="장부금액 감소 + 처분이익",
    desc="무형자산이 290 에서 200 으로 90 줄었다. 장부금액 90 짜리를 팔았는데 처분이익이 10 났으니 실제로 받은 돈은 100 이다. "
         "2장에서 영업활동에서 뺀 처분이익 10 이 여기에 들어온다. 자리만 옮긴 것이라 전체 현금에는 변화가 없다.",
    code=DATA_D + '''

book = -d["무형자산"]                      # 줄어든 장부금액 90
gain = pl["무형자산처분이익"]                # 처분이익 10
sell = book + gain
print("장부금액 감소:", book)
print("처분이익:", gain)
print("무형자산의 처분:", sell)''',
    tip="무형자산을 상각했거나 새로 취득한 것이 있으면 장부금액 증감에 그 금액이 섞인다. 이 예제는 상각과 취득이 없는 경우다.",
    talk=[dict(who="robo", state="thinking", text="삐빅, 90 짜리를 100 에 팔았다. 받은 돈은 100.")],
)

def stages(ns, out):
    bs = ns["bs"]
    t = bs[bs["계정과목"] == "무형자산"][["계정과목", "기초", "기말", "증감"]]
    import pandas as pd
    s = pd.DataFrame({"항목": ["장부금액 감소", "처분이익", "받은 현금"], "금액": [ns["book"], ns["gain"], ns["sell"]]})
    return [
        S("재무상태표", "무형자산 장부금액이 90 줄었다.", T(t, hl=("증감",))),
        S("처분이익 더하기", f"장부금액 {ns['book']} + 처분이익 {ns['gain']} = 받은 현금 {ns['sell']}.",
          T(s, rcls=["", "g4", "ok"], hl=("금액",))),
    ]
