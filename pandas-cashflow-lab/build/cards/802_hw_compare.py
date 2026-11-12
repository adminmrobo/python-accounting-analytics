from lib import *

CARD = dict(
    id="hw_compare", ch="8. 과제 안내", cmd='mine.merge(disclosed, on="활동")',
    title="내 결과와 공시를 나란히 놓고 차이를 설명한다", excel="두 표를 VLOOKUP 으로 붙이고 차이 열 만들기",
    desc="과제의 핵심 표다. 앱이 만든 활동별 합계와 공시된 현금흐름표의 활동별 합계를 merge 로 붙이고 차이 열을 만든다. "
         "아래는 흔히 나오는 경우를 지어낸 숫자로 보인 것이다. 앱은 이자를 낸 돈을 영업에 두었는데 회사는 재무활동으로 분류했고, 그래서 영업과 재무가 30 씩 반대로 어긋난다. "
         "세 활동의 차이를 더하면 0 이다. 총액은 맞고 분류만 다르다는 뜻이다. 차이의 합이 0 이 아니면 숫자를 잘못 읽었거나 빠진 계정이 있는 것이다.",
    code='''import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

mine = pd.DataFrame({"활동": ["영업활동", "투자활동", "재무활동"], "앱": [270, -500, 380]})
disclosed = pd.DataFrame({"활동": ["영업활동", "투자활동", "재무활동"], "공시": [300, -500, 350]})   # 지어낸 예

cmp = mine.merge(disclosed, on="활동")
cmp["차이"] = cmp["앱"] - cmp["공시"]
print(cmp)
print("차이의 합:", cmp["차이"].sum())

cmp["원인"] = ["이자 지급 30 을 회사는 재무활동으로 분류", "", "위와 같은 30 (반대 방향)"]
print(cmp[cmp["차이"] != 0][["활동", "차이", "원인"]].to_string(index=False))''',
    tip="차이의 원인으로 자주 나오는 것들: 이자·배당·법인세의 활동 분류, 유형자산 처분, 차입과 상환의 총액 표시, 리스, 외화환산, 대손상각비·퇴직급여 같은 비현금 항목, 현금이 오가지 않은 거래(주석의 '비현금거래'). 공시의 현금흐름표와 주석을 한 줄씩 읽으며 찾는다.",
    talk=[dict(who="fly", text="차이의 합이 0 이야? 그럼 분류 문제고, 아니면 숫자 문제야.")],
)

def stages(ns, out):
    cmp = ns["cmp"]
    return [
        S("두 결과", "앱의 합계와 공시의 합계.", T(ns["mine"], title="mine"), T(ns["disclosed"], title="disclosed")),
        S("merge 와 차이", f"영업 −30, 재무 +30. 차이의 합은 {cmp['차이'].sum()}.",
          T(cmp[["활동", "앱", "공시", "차이"]], hl=("차이",), rcls=["bad", "ok", "bad"]), links=[[0, 0], [1, 0]]),
        S("원인 적기", "차이가 있는 줄마다 원인을 한 줄로 적는다. 이 표가 보고서의 중심이다.", T(cmp[cmp["차이"] != 0][["활동", "차이", "원인"]])),
    ]
