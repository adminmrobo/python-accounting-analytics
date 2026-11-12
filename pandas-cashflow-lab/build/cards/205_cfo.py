from lib import *
from snippets import DATA_D

CARD = dict(
    id="cfo", ch="2. 영업활동: 간접법 다섯 계단", cmd="pd.concat([①, ②, ③, ④])",
    title="⑤ 계단을 이어 붙여 영업현금 270", excel="네 구역을 아래로 이어 붙이고 SUM",
    desc="지금까지 만든 조각은 모두 이름표가 붙은 Series 다. pd.concat 은 Series 여러 개를 위아래로 이어 붙인다. "
         "이어 붙인 것을 sum() 하면 영업활동 현금흐름이다. 순이익 170 이 270 이 되었는지 assert 로 확인한다.",
    code=DATA_D + '''
import numpy as np

ops = ["매출채권", "상품재고", "선급보험료", "매입채무", "미지급급여"]
wc = bs[bs["계정과목"].isin(ops)].set_index("계정과목")
wc_effect = pd.Series(np.where(wc["구분"] == "자산", -wc["증감"], wc["증감"]), index=wc.index)

cfo = pd.concat([
    pd.Series({"① 당기순이익": pl.sum()}),
    -pl[["감가상각비"]].add_prefix("② "),
    -pl.filter(like="처분").add_prefix("③ "),
    wc_effect.add_prefix("④ "),
])
print(cfo)
print("⑤ 영업활동 현금흐름:", cfo.sum())
assert cfo.sum() == 270''',
    tip="add_prefix 는 이름표 앞에 글자를 붙인다. 어느 계단에서 온 줄인지 표에 남겨 두면 나중에 틀린 곳을 찾기 쉽다.",
    talk=[dict(who="robo", state="success", text="삐빅! 170 에서 270. 계단 여덟 줄 합계 확인.")],
)

def stages(ns, out):
    cfo = ns["cfo"].rename("금액")
    t = cfo.rename_axis("항목").reset_index()
    cls = ["g5", "g2", "g4"] + ["g0"] * 3 + ["g1"] * 2
    return [
        S("네 조각", "① 순이익, ② 가산, ③ 차감, ④ 자산·부채 변동이 따로 있다.",
          T(t.iloc[:1]), T(t.iloc[1:3]), T(t.iloc[3:])),
        S("concat", "위아래로 이어 붙이면 영업활동 구역이 완성된다.", T(t, rcls=cls), links=[[0, 0], [1, 0], [2, 0]]),
        S("sum()", f"170 + 80 − 10 − 100 + 60 − 20 + 40 + 50 = {cfo.sum()}.", TX(out.splitlines()[-1], "out", "출력")),
    ]
