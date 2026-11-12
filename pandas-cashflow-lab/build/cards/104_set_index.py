from lib import *
from snippets import DATA

CARD = dict(
    id="set_index", ch="1. 재무제표를 표로 담기", cmd='set_index("계정과목")["증감"]',
    title="계정 이름으로 증감 꺼내 쓰기", excel="VLOOKUP 으로 계정 이름 찾아 값 가져오기",
    desc='set_index("계정과목") 은 계정과목 열을 이름표로 올린다. 거기서 증감 열만 뽑으면 d["매출채권"] 처럼 '
         "계정 이름으로 증감을 바로 꺼내는 Series 가 된다. 뒤의 계산식이 교재의 식과 같은 모양이 된다.",
    code=DATA + '''
bs["증감"] = bs["기말"] - bs["기초"]

d = bs.set_index("계정과목")["증감"]
print(d)
print("매출채권 증감:", d["매출채권"])
# 매출 2,100 중 외상으로 남은 100 을 빼면 실제로 받은 현금
print("매출로 받은 현금:", pl["매출액"] - d["매출채권"])''',
)

def stages(ns, out):
    bs, d = ns["bs"], ns["d"]
    return [
        S("표", "계정과목이 보통 열로 들어 있다.", T(bs[["계정과목", "증감"]])),
        S("이름표로 올리기", "계정과목이 이름표가 되고 값은 증감 하나만 남는다.",
          T(d, index=True, ix_name="계정과목", hl=("증감",))),
        S("이름으로 계산", f'pl["매출액"] − d["매출채권"] = 2100 − {d["매출채권"]} = {ns["pl"]["매출액"] - d["매출채권"]}. 식이 말과 같은 모양이다.',
          TX("\n".join(out.splitlines()[-2:]), "out", "출력")),
    ]
