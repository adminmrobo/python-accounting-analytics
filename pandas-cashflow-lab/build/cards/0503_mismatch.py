from lib import *

CARD = dict(
    id="mismatch", ch="5. 내 재무제표 불러오기", cmd='ni 와 d["현금"] 비교', chain=True,
    title="대차는 맞는데, 이익과 현금이 안 맞는다", excel="SUMIF 대차 확인과 두 셀 비교",
    desc="먼저 대차를 확인한다. 생성기가 만든 숫자는 기초와 기말 모두 자산 = 부채 + 자본 이 맞는다. "
         "그다음 당기순이익과 현금의 증감을 나란히 놓는다. 두 숫자는 거의 언제나 다르다. 이익이 났는데 현금이 줄기도 한다. "
         "이 차이를 계단으로 설명하는 것이 6장의 현금흐름표다.",
    code='''side = bs.groupby("구분")[["기초", "기말"]].sum()
gap = side.loc["자산"] - side.loc["부채"] - side.loc["자본"]
print(side)
print("대차가 맞는가:", gap.abs().sum() == 0)

print("당기순이익:", ni)
print("현금의 증감:", d["현금"], "(", b.loc["현금", "기초"], "→", b.loc["현금", "기말"], ")")
print("차이 (현금 증감 - 순이익):", d["현금"] - ni)''',
    xl=[
        ('bs.groupby("구분")[["기초", "기말"]].sum()', '=SUMIF($D$2:$D$13, "자산", G$2:G$13) 을 자산·부채·자본, 기초·기말마다 만든다.'),
        ("gap.abs().sum() == 0", "자산 합계 − 부채 합계 − 자본 합계 가 두 칸 모두 0 인가."),
        ('d["현금"]', "I2 셀 (현금의 증감)"),
        ('d["현금"] - ni', "=I2-SUM(J14:J21)"),
    ],
    talk=[
        dict(who="robo", state="confused", text="삐빅? 대차는 맞는데 이익과 현금 증감이 다르다."),
        dict(who="asst", text="박사님, 이익이 났는데 현금은 왜 이래요?"),
    ],
)

def stages(ns, out):
    import pandas as pd
    side, d, ni = ns["side"], ns["d"], ns["ni"]
    t = pd.DataFrame({"항목": ["당기순이익 (손익계산서)", "현금의 증감 (재무상태표)", "차이"], "금액": [ni, d["현금"], d["현금"] - ni]})
    return [
        S("대차 확인", f"기말 자산 {side.loc['자산', '기말']} = 부채 {side.loc['부채', '기말']} + 자본 {side.loc['자본', '기말']}. 맞는다.",
          T(side, index=True, rcls=["g2", "g1", "g0"])),
        S("이익 vs 현금", f"순이익은 {ni} 인데 현금은 {d['현금']} 변했다. 차이 {d['현금'] - ni}.",
          T(t, rcls=["ok", "bad", "hr"], hl=("금액",))),
    ]
