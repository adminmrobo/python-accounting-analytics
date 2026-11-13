"""엑셀 연습 통합 문서 두 권을 만든다. 카드의 '엑셀로 따라 하기' 표가 가리키는 셀이다.
- data/cashflow_by_excel.xlsx : 0~4장 (주)SG화학
- data/내회사_엑셀검산.xlsx    : 5~10장 학번 회사 (재무제표 시트에 내 CSV 를 붙여 넣으면 다시 계산된다)
usage: python build/make_excel.py"""
import csv, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))
from build import SAMPLE_ID

def make_sg_workbook():
    """코드와 같은 계산을 수식으로 넣은 엑셀 통합 문서. 카드의 '엑셀로 따라 하기' 가 가리키는 셀이다."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    wb = Workbook()
    bold, head = Font(bold=True), PatternFill("solid", fgColor="FFE9A3")
    def put(ws, rows, widths):
        for r in rows: ws.append(r)
        for c in ws[1]: c.font, c.fill = bold, head
        for i, wd in enumerate(widths): ws.column_dimensions["ABCDEFGHIJK"[i]].width = wd
    names = ["매출액", "매출원가", "보험료", "급여", "감가상각비", "기타영업비용", "이자비용", "무형자산처분이익"]
    amounts = [2100, -1100, -80, -550, -80, -100, -30, 10]
    ws = wb.active; ws.title = "손익계산서"
    put(ws, [["계정과목", "금액"]] + [[n, a] for n, a in zip(names, amounts)] + [["당기순이익", "=SUM(B2:B9)"]], [22, 12])
    ws = wb.create_sheet("재무상태표")
    acc = ["현금", "매출채권", "상품재고", "선급보험료", "유형자산", "감가상각누계액", "무형자산", "매입채무", "미지급급여", "차입금", "자본금", "이익잉여금"]
    side = ["자산"] * 7 + ["부채"] * 3 + ["자본"] * 2
    beg = [250, 230, 280, 10, 1000, -200, 290, 100, 20, 300, 1000, 440]
    end = [400, 330, 220, 30, 1600, -280, 200, 140, 70, 730, 1000, 560]
    kind = ["현금", "영업", "영업", "영업", "투자", "비현금", "투자", "영업", "영업", "재무", "재무", "이익잉여금"]
    rows = [["계정과목", "구분", "기초", "기말", "증감", "분류", "현금효과"]]
    for i in range(12):
        r = i + 2
        rows.append([acc[i], side[i], beg[i], end[i], f"=D{r}-C{r}", kind[i], f'=IF(B{r}="자산",-E{r},E{r})'])
    rows += [[], ["자산 합계", "", '=SUMIF($B$2:$B$13,"자산",C$2:C$13)', '=SUMIF($B$2:$B$13,"자산",D$2:D$13)'],
             ["부채 + 자본 합계", "", "=SUM(C2:C13)-C15", "=SUM(D2:D13)-D15"],
             ["차이 (0 이어야 한다)", "", "=C15-C16", "=D15-D16"]]
    put(ws, rows, [22, 8, 10, 10, 10, 12, 12])
    ws = wb.create_sheet("현금흐름표")
    put(ws, [["활동", "항목", "금액"],
             ["영업활동", "① 당기순이익", "=손익계산서!B10"],
             ["영업활동", "② 감가상각비 가산", "=-손익계산서!B6"],
             ["영업활동", "③ 무형자산처분이익 차감", "=-손익계산서!B9"],
             ["영업활동", "④ 영업 관련 자산·부채 변동", '=SUMIF(재무상태표!F2:F13,"영업",재무상태표!G2:G13)'],
             ["", "영업활동 현금흐름", "=SUM(C2:C5)"],
             ["투자활동", "유형자산의 취득", "=재무상태표!G6"],
             ["투자활동", "무형자산의 처분", "=재무상태표!G8+손익계산서!B9"],
             ["", "투자활동 현금흐름", "=SUM(C7:C8)"],
             ["재무활동", "차입금의 순증가", "=재무상태표!G11"],
             ["재무활동", "배당금의 지급", "=-(재무상태표!C13+손익계산서!B10-재무상태표!D13)"],
             ["", "재무활동 현금흐름", "=SUM(C10:C11)"],
             ["", "현금의 증가", "=C6+C9+C12"],
             ["", "기초의 현금", "=재무상태표!C2"],
             ["", "기말의 현금", "=C13+C14"],
             ["", "검산 (기말 현금 = 재무상태표)", '=IF(C15=재무상태표!D2,"통과","실패")']], [12, 32, 12])
    wb.save(os.path.join(ROOT, "data", "cashflow_by_excel.xlsx"))


def make_my_workbook():
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    bold, head, note = Font(bold=True), PatternFill("solid", fgColor="FFE9A3"), Font(italic=True, color="666666")
    rows = list(csv.reader(open(os.path.join(ROOT, "build", "sample", f"재무제표_{SAMPLE_ID}.csv"), encoding="utf-8-sig")))
    wb = Workbook()
    ws = wb.active; ws.title = "재무제표"
    for r in rows:
        ws.append([int(v) if v.lstrip("-").isdigit() else v for v in r])
    ws["I1"], ws["J1"] = "증감", "부호 붙인 금액"
    for r in range(2, 14): ws[f"I{r}"] = f"=H{r}-G{r}"
    for r in range(14, 22): ws[f"J{r}"] = f'=IF(D{r}="수익",H{r},-H{r})'
    ws["A23"] = f"← 생성기에서 받은 내 CSV 를 엑셀로 열어 A1:H21 을 복사해 이 시트의 A1 에 붙여 넣는다 (지금은 표본 학번 {SAMPLE_ID}). I·J 열과 다른 시트는 자동으로 다시 계산된다."
    ws["A23"].font = note
    for c in ws[1]: c.font, c.fill = bold, head
    for col, w in zip("ABCDEFGHIJ", [11, 14, 11, 7, 7, 16, 9, 9, 9, 14]): ws.column_dimensions[col].width = w
    F = "재무제표!"
    ws = wb.create_sheet("현금흐름표")
    lines = [["활동", "항목", "금액"],
        ["영업활동", "① 당기순이익", f"=SUM({F}J14:J21)"],
        ["영업활동", "② 감가상각비 가산", f"={F}H18"],
        ["영업활동", "③ 무형자산처분이익 차감", f"=-{F}H21"],
        ["영업활동", "④ 매출채권 증감", f"=-{F}I3"],
        ["영업활동", "④ 상품재고 증감", f"=-{F}I4"],
        ["영업활동", "④ 선급보험료 증감", f"=-{F}I5"],
        ["영업활동", "④ 매입채무 증감", f"={F}I9"],
        ["영업활동", "④ 미지급급여 증감", f"={F}I10"],
        ["투자활동", "유형자산의 취득", f"=-{F}I6"],
        ["투자활동", "무형자산의 처분", f"=-{F}I8+{F}H21"],
        ["재무활동", "차입금의 순증감", f"={F}I11"],
        ["재무활동", "유상증자", f"={F}I12"],
        ["재무활동", "배당금의 지급", f"=-({F}G13+C2-{F}H13)"],
        [],
        ["합계", "영업활동 현금흐름", '=SUMIF(A2:A14,"영업활동",C2:C14)'],
        ["합계", "투자활동 현금흐름", '=SUMIF(A2:A14,"투자활동",C2:C14)'],
        ["합계", "재무활동 현금흐름", '=SUMIF(A2:A14,"재무활동",C2:C14)'],
        ["", "현금의 증가 (세 활동 합계)", "=SUM(C16:C18)"],
        ["", "현금 증감 (재무상태표)", f"={F}I2"],
        ["", "검산", '=IF(C19=C20,"통과","실패")']]
    for r in lines: ws.append(r)
    for c in ws[1]: c.font, c.fill = bold, head
    ws.column_dimensions["A"].width, ws.column_dimensions["B"].width, ws.column_dimensions["C"].width = 10, 28, 10
    ws = wb.create_sheet("재무비율")
    S = lambda gu, se, col: f'SUMIFS({F}{col}2:{col}13,{F}D2:D13,"{gu}",{F}E2:E13,"{se}")'
    T = lambda gu, col: f'SUMIF({F}D2:D13,"{gu}",{F}{col}2:{col}13)'
    op = f'SUMIF({F}E14:E21,"영업",{F}J14:J21)'
    ni, sales, cogs = f"SUM({F}J14:J21)", f"{F}H14", f"{F}H15"
    avgA, avgE = f"(({T('자산','G')})+({T('자산','H')}))/2", f"(({T('자본','G')})+({T('자본','H')}))/2"
    ratios = [
        ["안정성", "유동비율", f"={S('자산','유동','H')}/{S('부채','유동','H')}*100", "%", 150, "이상"],
        ["안정성", "부채비율", f"={T('부채','H')}/{T('자본','H')}*100", "%", 200, "이하"],
        ["안정성", "자기자본비율", f"={T('자본','H')}/{T('자산','H')}*100", "%", 40, "이상"],
        ["안정성", "이자보상배율", f"={op}/{F}H20", "배", 3, "이상"],
        ["수익성", "매출총이익률", f"=({sales}-{cogs})/{sales}*100", "%", 25, "이상"],
        ["수익성", "영업이익률", f"={op}/{sales}*100", "%", 5, "이상"],
        ["수익성", "순이익률", f"={ni}/{sales}*100", "%", 3, "이상"],
        ["수익성", "ROA", f"={ni}/({avgA})*100", "%", 3, "이상"],
        ["수익성", "ROE", f"={ni}/({avgE})*100", "%", 8, "이상"],
        ["활동성", "매출채권회전율", f"={sales}/AVERAGE({F}G3:H3)", "회", 6, "이상"],
        ["활동성", "재고자산회전율", f"={cogs}/AVERAGE({F}G4:H4)", "회", 6, "이상"],
        ["활동성", "총자산회전율", f"={sales}/({avgA})", "회", 1, "이상"],
        ["현금흐름", "영업현금흐름/순이익", "=현금흐름표!C16/현금흐름표!C2", "배", 1, "이상"]]
    ws.append(["분류", "비율", "값", "단위", "기준", "방향", "판정"])
    for i, r in enumerate(ratios):
        n = i + 2
        r = r[:2] + ["=ROUND(" + r[2][1:] + ",1)"] + r[3:]          # 파이썬의 round(1) 과 같게
        ws.append(r + [f'=IF(F{n}="이상",IF(C{n}>=E{n},"양호","주의"),IF(C{n}<=E{n},"양호","주의"))'])
        ws[f"C{n}"].number_format = "0.0"
    for c in ws[1]: c.font, c.fill = bold, head
    for col, w in zip("ABCDEFG", [10, 20, 10, 6, 7, 7, 8]): ws.column_dimensions[col].width = w
    wb.save(os.path.join(ROOT, "data", "내회사_엑셀검산.xlsx"))

if __name__ == "__main__":
    import subprocess
    subprocess.run(["node", os.path.join(ROOT, "build", "gen_sample.js"), SAMPLE_ID], check=True, capture_output=True)
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    make_sg_workbook()
    make_my_workbook()
    print("data/cashflow_by_excel.xlsx, data/내회사_엑셀검산.xlsx")
