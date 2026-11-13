from lib import *
from snippets import CF_PARTS

CARD = dict(
    id="subtotal", ch="4. 조립하고 검산하기", cmd="groupby 소계 + concat + sort_values",
    title="활동마다 소계를 넣어 보고서 모양으로", excel="부분합 (데이터 → 부분합)",
    desc="제출하는 현금흐름표에는 활동별 소계와 맨 아래 현금의 증가, 기초·기말 현금이 있어야 한다. "
         "먼저 groupby 로 소계 세 줄을 만든다. 원래 줄에는 차례 0, 소계 줄에는 차례 1 을 붙여 한 표로 합친 뒤, 활동 번호와 차례로 정렬하면 소계가 각 활동의 끝에 놓인다. "
         "마지막에 현금의 증가, 기초 현금 250, 기말 현금 400 을 붙이면 양식이 완성된다.",
    code=CF_PARTS + '''

cf = pd.concat({"영업활동": cfo, "투자활동": cfi, "재무활동": cff}, names=["활동", "항목"]).rename("금액").reset_index()
cf["차례"] = 0                                                   # 원래 줄

sub = cf.groupby("활동", sort=False, as_index=False)["금액"].sum()  # 활동별 소계 세 줄
sub["항목"] = sub["활동"] + " 현금흐름"
sub["차례"] = 1                                                  # 소계 줄은 뒤로

both = pd.concat([cf, sub])
both["활동번호"] = both["활동"].map({"영업활동": 1, "투자활동": 2, "재무활동": 3})
both = both.sort_values(["활동번호", "차례"], kind="stable")

increase = cf["금액"].sum()
tail = pd.DataFrame()
tail["항목"] = ["현금의 증가", "기초의 현금", "기말의 현금"]
tail["금액"] = [increase, 250, 250 + increase]
report = pd.concat([both[["항목", "금액"]], tail], ignore_index=True)
print(report.to_string(index=False))
print("기말 현금이 재무상태표와 같은가:", report["금액"].iloc[-1] == 400)''',
    xl=[
        ('cf.groupby("활동", as_index=False)["금액"].sum()', "데이터 → 부분합(그룹화할 항목: 활동, 사용할 함수: 합계, 계산 항목: 금액). 또는 활동마다 =SUM( ) 줄을 직접 넣는다."),
        ('sub["항목"] = sub["활동"] + " 현금흐름"', '=A2 & " 현금흐름" 으로 소계 줄의 이름을 만든다.'),
        ('cf["차례"] = 0, sub["차례"] = 1, sort_values([...])', "보조 열에 활동 번호와 차례를 적고, 데이터 → 정렬에서 활동 번호 → 차례 순으로 정렬한다. 소계가 각 활동 끝으로 간다."),
        ("tail (현금의 증가 · 기초 · 기말)", "연습 파일 현금흐름표의 C13 =C6+C9+C12, C14 =재무상태표!C2, C15 =C13+C14"),
    ],
    tip='report.to_excel("cashflow.xlsx", index=False) 한 줄이면 엑셀 파일로 저장된다. 7장에서 내려받기 버튼으로 만든다.',
)

def stages(ns, out):
    cf, rp, sub = ns["cf"], ns["report"], ns["sub"]
    is_sub = rp["항목"].str.contains("현금흐름|현금의|의 현금")
    return [
        S("줄만 있는 표", "13 줄이 이어져 있고 소계가 없다.", T(cf[["활동", "항목", "금액"]])),
        S("소계 세 줄", "groupby 로 활동마다 합계를 낸다.", T(sub[["활동", "항목", "금액"]], rcls=["hr"] * 3)),
        S("합치고 정렬", "소계가 각 활동의 끝에 놓이고, 맨 아래에 현금의 증가와 기초·기말 현금이 붙었다. 마지막 줄 400 이 재무상태표의 기말 현금이다.",
          T(rp, rcls=["hr" if s else "" for s in is_sub])),
    ]
