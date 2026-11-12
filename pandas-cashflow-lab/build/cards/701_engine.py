from lib import *
from snippets import RAW, TOOLS, ENGINE

CARD = dict(
    id="engine", ch="7. 앱으로 만들기", cmd="make_cashflow(pl, bs)",
    title="분류가 붙은 표 두 장을 넣으면 현금흐름표가 나오는 함수", excel="수식을 다 걸어 둔 템플릿 시트",
    desc="2~4장에서 손으로 한 일을 함수 하나로 묶는다. 입력은 분류 열이 붙은 손익계산서와 재무상태표다. 분류만 보고 계산하므로 계정 이름이 달라도 된다. "
         "재무상태표의 모든 계정에 '현금효과'(자산 증가는 −, 부채·자본 증가는 +)를 만들고, 분류에 따라 영업·투자·재무 구역으로 보낸다. "
         "함수는 현금흐름표와 검산표를 함께 돌려준다. 검산은 넷이다. A 대차 일치, B 미분류 없음, C 세 활동 합계 = 현금 증감, D 비현금비용 = 비현금 계정 증감. "
         "주석이 없어 차입과 상환을 나누지 못하므로 재무·투자 항목은 순증감으로 적는다.",
    code=RAW + "\n" + TOOLS.replace("import pandas as pd\n", "") + "\n\n" + ENGINE + '''

pl = tidy_pl(raw_pl)
bs = tidy_bs(raw_bs)
cf, checks = make_cashflow(pl, bs)
print(cf.to_string(index=False))
print(cf.groupby("활동", sort=False)["금액"].sum().to_dict())
print(checks.to_string(index=False))''',
    tip="검산 D 가 틀리면 C 도 같은 금액만큼 틀린다. 올해 처분한 유형자산이 있거나 상각비 말고 다른 비현금 항목이 있다는 신호다. 주석에서 원인을 찾아 분류를 고치거나 항목을 더한다. 검산 C 는 분류가 틀려도 통과할 수 있다. 영업을 투자로 잘못 분류해도 합계는 같기 때문이다. 그래서 과제에서는 공시된 현금흐름표와 활동별로 대조한다.",
    talk=[
        dict(who="asst", text="계정 이름이 회사마다 다른데 함수 하나로 돼요?"),
        dict(who="doc", text="이름이 아니라 분류를 보고 계산하니까요. 분류만 맞으면 돼요."),
    ],
)

def stages(ns, out):
    pl, bs, cf, ck = ns["pl"], ns["bs"], ns["cf"], ns["checks"]
    g = {"영업활동": "g0", "투자활동": "g1", "재무활동": "g2"}
    return [
        S("입력 두 장", "5장의 정리 도구가 만든 표. 분류 열이 붙어 있다.", T(pl, hl=("분류",)), T(bs, hl=("분류",))),
        S("현금흐름표", "분류에 따라 세 구역으로 나뉜다. 영업 270, 투자 −500, 재무 380.",
          T(cf, rcls=[g[a] for a in cf["활동"]]), links=[[0, 0], [1, 0]]),
        S("검산표", "네 검산의 계산값과 기준값이 모두 같다.", T(ck, rcls=["ok" if p else "bad" for p in ck["통과"]], hl=("통과",))),
    ]
