from lib import *

CARD = dict(
    id="pl_series", ch="1. 재무제표를 표로 담기", cmd="pd.Series(금액, index=계정과목).sum()",
    title="손익계산서를 한 줄짜리 표로", excel="A열 계정과목, B열 금액, 맨 아래 SUM",
    desc="Series 는 이름표(index)가 붙은 한 줄짜리 표다. 엑셀로 치면 A열에 계정과목, B열에 금액을 적은 것과 같다. "
         "비용을 음수로 적어 두면 sum() 한 번으로 당기순이익이 나오고, 뒤에서 부호를 헷갈릴 일이 줄어든다. "
         'pl["감가상각비"] 처럼 계정 이름으로 값을 꺼낸다.',
    code='''import pandas as pd

# (주)SG화학 2014년 손익계산서 (원). 수익은 +, 비용은 −
names = ["매출액", "매출원가", "보험료", "급여", "감가상각비", "기타영업비용", "이자비용", "무형자산처분이익"]
amounts = [2100, -1100, -80, -550, -80, -100, -30, 10]
pl = pd.Series(amounts, index=names, name="금액")
print(pl)
print("당기순이익:", pl.sum())
print("감가상각비:", pl["감가상각비"])''',
    xl=[
        ("names = [...]", "A2:A9 에 계정과목 여덟 개를 적는다."),
        ("amounts = [...]", "B2:B9 에 금액을 적는다. 비용 여섯 개는 음수."),
        ("pl = pd.Series(amounts, index=names)", "A열과 B열을 나란히 둔 표가 곧 pl 이다. A열이 이름표다."),
        ("pl.sum()", "B10 에 =SUM(B2:B9) → 170"),
        ('pl["감가상각비"]', '=VLOOKUP("감가상각비", A2:B9, 2, FALSE) → −80. 이름으로 값을 찾는다.'),
    ],
    tip="교재나 공시의 손익계산서는 비용도 양수로 적혀 있다. 옮겨 적을 때 비용에 − 를 붙이는 일을 5장에서 코드로 자동화한다.",
    talk=[
        dict(who="asst", text="비용을 왜 음수로 적어요? 책에는 양수로 나와요."),
        dict(who="doc", text="전부 더하기만 하면 순이익이 나오게 하려고요."),
    ],
)

def stages(ns, out):
    pl = ns["pl"]
    return [
        S("이름표와 값", "계정과목이 이름표(index), 금액이 값이다. 비용 여섯 줄은 음수다.",
          T(pl, index=True, ix_name="계정과목")),
        S("sum()", f"모두 더하면 2100 − 1100 − 80 − 550 − 80 − 100 − 30 + 10 = {pl.sum()}. 당기순이익이다.",
          TX(f"당기순이익: {pl.sum()}", "out", "pl.sum()")),
        S("이름으로 꺼내기", 'pl["감가상각비"] 는 이름표가 감가상각비인 값 하나를 돌려준다.',
          T(pl, index=True, ix_name="계정과목", hlrows=[4]), TX(out.splitlines()[-1], "out", "출력")),
    ]
