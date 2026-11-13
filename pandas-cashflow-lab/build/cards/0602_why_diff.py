from lib import *

CARD = dict(
    id="why_diff", ch="6. 내 회사의 현금흐름표", cmd='sort_values("크기", ascending=False).head(3)', chain=True,
    title="검산하고, 이익과 현금이 다른 이유 세 가지를 찾는다", excel="정렬(내림차순)과 상위 3개",
    desc="먼저 4장의 검산을 한다. 세 활동의 합이 현금 증감과 같아야 한다. "
         "그다음 순이익과 영업현금의 차이를 만든 조정 항목(②~④) 중 크기가 큰 세 개를 고른다. 금액의 절댓값(abs)으로 크기 열을 만들고 큰 순서로 정렬해 위의 세 줄을 본다. "
         "이 세 줄이 5장에서 본 '이익과 현금이 안 맞는' 이유이고, 10장 보고서의 핵심 문장이 된다.",
    code='''print("세 활동 합계:", total.sum(), "| 현금 증감:", d["현금"], "| 검산 통과:", total.sum() == d["현금"])
cfo = total["영업활동"]
print("당기순이익:", ni, "→ 영업활동 현금흐름:", cfo, "| 차이:", cfo - ni)

adj = cf[cf["항목"].str[0].isin(["②", "③", "④"])].copy()    # 조정 항목만
adj["크기"] = adj["금액"].abs()
top3 = adj.sort_values("크기", ascending=False).head(3)
print(top3[["항목", "금액"]])''',
    xl=[
        ("total.sum() == d[\"현금\"]", "'현금흐름표' C19: =SUM(C16:C18), C20: =재무제표!I2, C21: =IF(C19=C20, \"통과\", \"실패\")"),
        ("cfo - ni", "=C16-C2"),
        ('cf["항목"].str[0].isin(["②", "③", "④"])', "C3:C9 (조정 일곱 줄)을 고른다."),
        ('adj["금액"].abs()', "D3 에 =ABS(C3) 를 넣고 D9 까지 채운다."),
        ('sort_values("크기", ascending=False).head(3)', "=LARGE(D3:D9, 1), =LARGE(D3:D9, 2), =LARGE(D3:D9, 3). 또는 D열 기준 내림차순 정렬 후 위 세 줄."),
    ],
    talk=[
        dict(who="sia", text="판정. 세 활동 합계와 현금 증감, 일치합니다."),
        dict(who="fly", text="큰 세 줄만 봐도 이유가 보여. 외상이 늘었는지, 재고가 쌓였는지."),
    ],
)

def stages(ns, out):
    import pandas as pd
    adj, top3 = ns["adj"], ns["top3"]
    lines = out.splitlines()
    big = set(top3.index)
    return [
        S("검산", "세 활동의 합이 현금 증감과 같다.", TX("\n".join(lines[:2]), "out", "출력")),
        S("조정 항목", "②~④ 일곱 줄에 크기(절댓값) 열을 붙였다.", T(adj[["항목", "금액", "크기"]], hl=("크기",))),
        S("큰 세 줄", "이익과 현금을 가장 크게 벌린 항목이다.",
          T(adj[["항목", "금액", "크기"]], rcls=["hr" if i in big else "dim" for i in adj.index]), T(top3[["항목", "금액"]], rcls=["bad"] * 3)),
    ]
