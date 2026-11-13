from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="assemble", ch="4. 조립하고 검산하기", cmd='pd.concat({"영업활동": cfo, ...})',
    title="세 구역을 한 장의 현금흐름표로", excel="세 구역을 한 시트에 쌓고 활동 열 추가",
    desc="concat 에 사전을 넣으면 사전의 키가 바깥 이름표가 된다. 영업·투자·재무 세 Series 를 넣으면 "
         "활동과 항목 두 겹 이름표가 붙은 한 줄짜리 표가 되고, reset_index 로 보통 표(활동, 항목, 금액)로 편다. "
         "이 모양이면 groupby 로 활동별 합계를 바로 낼 수 있다.",
    code=CF_PARTS + '''

cf = pd.concat({"영업활동": cfo, "투자활동": cfi, "재무활동": cff}, names=["활동", "항목"])
cf = cf.rename("금액").reset_index()
print(cf)
total = cf.groupby("활동", sort=False)["금액"].sum()
print(total)''',
    xl=[
        ('pd.concat({"영업활동": cfo, "투자활동": cfi, "재무활동": cff})', "세 구역을 한 시트에 위에서 아래로 붙인다. A열에 활동 이름(영업활동·투자활동·재무활동)을 줄마다 적는다."),
        ('.rename("금액").reset_index()', "첫 줄에 머리글 활동 · 항목 · 금액을 적는다. A, B, C 세 열짜리 보통 표가 된다."),
        ('cf.groupby("활동", sort=False)["금액"].sum()', '=SUMIF(A:A, "영업활동", C:C) 를 활동마다 만든다. 피벗 테이블(행: 활동, 값: 금액 합계)도 같다.'),
    ],
    tip="groupby 는 기본으로 이름을 가나다순으로 정렬한다. sort=False 를 주면 표에 나온 순서(영업 → 투자 → 재무)가 유지된다.",
    talk=[
        dict(who="asst", text="조각이 셋인데 표 하나로 합칠 수 있어요?"),
        dict(who="doc", text="활동 이름을 키로 주고 이어 붙이면 돼요."),
    ],
)

def stages(ns, out):
    cf, total = ns["cf"], ns["total"]
    g = {"영업활동": "g0", "투자활동": "g1", "재무활동": "g2"}
    def one(s, c): return T(s.rename("금액"), index=True, ix_name="항목", rcls=[c] * len(s))
    return [
        S("세 구역", "영업 여덟 줄, 투자 두 줄, 재무 세 줄이 따로 있다.", one(ns["cfo"], "g0"), one(ns["cfi"], "g1"), one(ns["cff"], "g2")),
        S("concat", "키가 활동 열이 되어 한 표로 쌓인다.", T(cf, rcls=[g[a] for a in cf["활동"]]), links=[[0, 0], [1, 0], [2, 0]]),
        S("활동별 합계", f"영업 {total['영업활동']}, 투자 {total['투자활동']}, 재무 {total['재무활동']}.",
          T(total, index=True, ix_name="활동", rcls=["g0", "g1", "g2"], hl=("금액",))),
    ]
