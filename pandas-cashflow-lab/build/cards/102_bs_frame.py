from lib import *
from snippets import DATA

CARD = dict(
    id="bs_frame", ch="1. 재무제표를 표로 담기", cmd='groupby("구분")[["기초", "기말"]].sum()',
    title="재무상태표를 담고 대차부터 맞춘다", excel="SUMIF 로 자산 합계와 부채·자본 합계 비교",
    desc="재무상태표는 열이 여러 개라 DataFrame 에 담는다. 계정과목, 구분(자산·부채·자본), 기초, 기말 네 열이면 충분하다. "
         "담자마자 할 일은 대차 확인이다. 구분별 합계를 내서 자산 = 부채 + 자본 이 기초와 기말 모두에서 맞는지 본다. "
         "여기서 틀리면 뒤의 현금흐름표는 반드시 틀린다. 감가상각누계액은 자산을 깎는 계정이라 음수로 적는다.",
    code=DATA + '''

side = bs.groupby("구분")[["기초", "기말"]].sum()
print(side)
gap = side.loc["자산"] - (side.loc["부채"] + side.loc["자본"])
print("자산 - (부채 + 자본):", gap.tolist())
assert (gap == 0).all(), "대차가 맞지 않는다. 옮겨 적은 숫자를 다시 본다"''',
    tip="assert 는 조건이 거짓이면 그 자리에서 멈추고 뒤의 글을 보여 준다. 숫자를 옮겨 적은 직후에 한 줄 넣어 두면 오타를 바로 잡는다.",
    talk=[dict(who="fly", text="한 칸만 잘못 옮겨도 뒤가 전부 틀려. 대차부터 봐.")],
)

def stages(ns, out):
    bs, side = ns["bs"], ns["side"]
    g = {"자산": "g0", "부채": "g1", "자본": "g2"}
    return [
        S("재무상태표", "열두 계정이 자산 · 부채 · 자본 세 묶음이다. 같은 구분은 같은 색이다.",
          T(bs, rcls=[g[x] for x in bs["구분"]])),
        S("구분별 합계", f"groupby 로 구분마다 기초와 기말을 더한다. 기말 자산은 {side.loc['자산', '기말']}.",
          T(side, index=True, rcls=["g2", "g1", "g0"])),
        S("대차 확인", f"자산 {side.loc['자산', '기말']} = 부채 {side.loc['부채', '기말']} + 자본 {side.loc['자본', '기말']}. 차이가 0 이면 통과.",
          TX(out.splitlines()[-1], "out", "출력")),
    ]
