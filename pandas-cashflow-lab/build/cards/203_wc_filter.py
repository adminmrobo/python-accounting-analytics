from lib import *
from snippets import DATA_D

CARD = dict(
    id="wc_filter", ch="2. 영업활동: 간접법 다섯 계단", cmd="bs[bs[\"계정과목\"].isin(ops)]",
    title="④ 영업 관련 계정만 고른다", excel="필터에서 여러 항목 체크",
    desc="④ 계단에 들어가는 것은 영업과 관련된 자산·부채다. 매출채권, 재고, 선급비용, 매입채무, 미지급비용 같은 계정이다. "
         "현금 자체, 유형자산·무형자산(투자), 차입금·자본(재무)은 여기에 넣지 않는다. "
         "isin 은 목록에 있는 이름인지 줄마다 True/False 로 답하고, 그 답으로 줄을 거른다.",
    code=DATA_D + '''

ops = ["매출채권", "상품재고", "선급보험료", "매입채무", "미지급급여"]
mask = bs["계정과목"].isin(ops)
print(mask.tolist())
wc = bs[mask]
print(wc)''',
    tip="어느 계정이 영업 관련인지 정하는 일이 간접법에서 가장 판단이 필요한 부분이다. 6장에서 이 분류를 생성AI 에게 맡기고, 사람이 검토하는 방식으로 바꾼다.",
    talk=[
        dict(who="asst", text="차입금도 부채인데 왜 빠져요?"),
        dict(who="doc", text="빌리고 갚는 일은 재무활동이에요. 영업에 쓰는 부채만 골라요."),
    ],
)

def stages(ns, out):
    bs, mask = ns["bs"], ns["mask"]
    v = bs[["계정과목", "구분", "증감"]]
    return [
        S("모든 계정", "열두 계정에 현금, 영업, 투자, 재무가 섞여 있다.", T(v)),
        S("isin(ops)", "목록에 있는 다섯 계정만 True 다.",
          T(v.assign(mask=mask), rcls=["ok" if m else "dim" for m in mask], hl=("mask",))),
        S("영업 관련 계정", "자산 셋, 부채 둘이 남았다.", T(ns["wc"][["계정과목", "구분", "증감"]])),
    ]
