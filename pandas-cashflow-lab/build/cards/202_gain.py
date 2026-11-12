from lib import *
from snippets import DATA_D

CARD = dict(
    id="gain", ch="2. 영업활동: 간접법 다섯 계단", cmd='pl.filter(like="처분")',
    title="③ 영업이 아닌 손익을 되돌린다", excel="처분이익을 음수로 다시 적기",
    desc="무형자산을 팔아 생긴 이익 10 은 순이익에 들어 있지만 영업으로 번 돈이 아니다. 판 돈 전체는 투자활동에 적으므로 "
         "영업활동에서는 이익을 뺀다. 그대로 두면 같은 돈을 두 번 세게 된다. "
         'filter(like="처분") 은 이름에 처분이 들어간 줄만 고른다. 처분손실이면 반대로 더해지는데, 부호를 뒤집는 식 하나로 둘 다 처리된다.',
    code=DATA_D + '''

gain = pl.filter(like="처분")          # 이름에 '처분' 이 들어간 손익
print(gain)
reverse = -gain                        # ③ 영업활동에서 되돌린다
print(reverse)''',
    talk=[dict(who="fly", text="처분이익을 안 빼면 영업에도 투자에도 들어가. 두 번 세는 거야.")],
)

def stages(ns, out):
    pl = ns["pl"]
    return [
        S("손익계산서", "마지막 줄 무형자산처분이익 +10 은 영업 밖에서 생긴 이익이다.",
          T(pl, index=True, ix_name="계정과목", hlrows=[7])),
        S('filter(like="처분")', "이름에 처분이 들어간 줄만 남는다.", T(ns["gain"], index=True, ix_name="계정과목")),
        S("되돌리기", "부호를 뒤집어 −10. 이 10 은 3장에서 투자활동의 처분 대금 100 안에 들어간다.",
          T(ns["reverse"], index=True, ix_name="③ 차감", hl=("금액",))),
    ]
