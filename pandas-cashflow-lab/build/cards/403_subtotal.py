from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="subtotal", ch="4. 조립하고 검산하기", cmd="groupby + concat 으로 소계 줄 넣기",
    title="활동마다 소계를 넣어 보고서 모양으로", excel="부분합 (데이터 → 부분합)",
    desc="제출하는 현금흐름표에는 활동별 소계와 맨 아래 현금의 증가, 기초·기말 현금이 있어야 한다. "
         "활동별로 표를 나눠 소계 줄을 하나씩 붙이고 다시 이어 붙인다. 마지막에 기초 현금 250 과 기말 현금 400 을 붙이면 양식이 완성된다.",
    code=CF_PARTS + '''

cf = pd.concat({"영업활동": cfo, "투자활동": cfi, "재무활동": cff}, names=["활동", "항목"]).rename("금액").reset_index()

blocks = []
for act, g in cf.groupby("활동", sort=False):
    blocks.append(g[["항목", "금액"]])
    blocks.append(pd.DataFrame({"항목": [act + " 현금흐름"], "금액": [g["금액"].sum()]}))
cash = bs.set_index("계정과목").loc["현금"]
blocks.append(pd.DataFrame({"항목": ["현금의 증가", "기초의 현금", "기말의 현금"],
                            "금액": [cf["금액"].sum(), cash["기초"], cash["기초"] + cf["금액"].sum()]}))
report = pd.concat(blocks, ignore_index=True)
print(report.to_string(index=False))
assert report["금액"].iloc[-1] == cash["기말"]''',
    tip='report.to_excel("cashflow.xlsx", index=False) 한 줄이면 엑셀 파일로 저장된다. 7장에서 내려받기 버튼으로 만든다.',
)

def stages(ns, out):
    cf, rp = ns["cf"], ns["report"]
    sub = rp["항목"].str.contains("현금흐름|현금의|의 현금")
    return [
        S("줄만 있는 표", "13 줄이 이어져 있고 소계가 없다.", T(cf[["항목", "금액"]])),
        S("소계 넣기", "활동마다 합계 줄을 붙이고, 끝에 현금의 증가와 기초·기말 현금을 붙였다. 마지막 줄 400 이 재무상태표의 기말 현금이다.",
          T(rp, rcls=["hr" if s else "" for s in sub])),
    ]
