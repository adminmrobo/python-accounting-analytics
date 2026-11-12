from lib import *
from snippets import RAW

CARD = dict(
    id="pdf_tables", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd="page.extract_tables()",
    title="PDF 속의 표를 DataFrame 으로", excel="데이터 → 데이터 가져오기 → PDF 에서",
    desc="감사보고서는 대부분 PDF 다. pdfplumber 는 PDF 쪽마다 선으로 그려진 표를 찾아 줄과 칸으로 나눠 준다. "
         "extract_tables 의 결과는 [표][줄][칸] 모양의 리스트라, 첫 줄을 열 이름으로 써서 DataFrame 으로 만든다. "
         "연습용 PDF 는 reportlab 으로 직접 만든다. 두 라이브러리는 Colab 에 없으니 먼저 설치한다.",
    code="# Colab 에서는 이 줄을 새 셀에서 먼저 실행한다:  !pip -q install pdfplumber reportlab\n" + RAW + '''
import pdfplumber
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import SimpleDocTemplate, Spacer, Table

# 연습용 PDF 만들기: 재무상태표와 손익계산서 표 두 개
pdfmetrics.registerFont(UnicodeCIDFont("HYGothic-Medium"))          # 한글 글꼴
style = [("FONTNAME", (0, 0), (-1, -1), "HYGothic-Medium"), ("GRID", (0, 0), (-1, -1), 0.5, (0, 0, 0))]
def as_rows(df):
    return [list(df.columns)] + df.fillna("").values.tolist()
SimpleDocTemplate("sg_2014.pdf", pagesize=A4).build(
    [Table(as_rows(raw_bs), style=style), Spacer(1, 20), Table(as_rows(raw_pl), style=style)])

# PDF 에서 표 꺼내기
with pdfplumber.open("sg_2014.pdf") as pdf:
    found = []
    for page in pdf.pages:
        found += page.extract_tables()
print("표 개수:", len(found), "| 줄 수:", [len(t) for t in found])
tables = [pd.DataFrame(t[1:], columns=t[0]) for t in found]         # 첫 줄을 열 이름으로
print(tables[0].head(8))''',
    tip="표에 선이 없는 PDF 는 extract_tables 가 표를 못 찾는다. 그때는 page.extract_text() 로 글자를 통째로 꺼내 생성AI 에게 넘긴다. 스캔한 그림 PDF 는 글자가 아예 없어 PDF 파일 자체를 AI 에게 보내야 한다.",
    talk=[dict(who="fly", text="PDF 에서 꺼낸 빈칸은 NaN 이 아니라 빈 글자야. 머리말 줄 찾을 때 조심해.")],
)

def stages(ns, out):
    tb = ns["tables"]
    return [
        S("PDF 파일", "한 쪽에 표 두 개가 선으로 그려져 있다.", TX("sg_2014.pdf\n └ 1쪽\n    ├ 재무상태표 (표)\n    └ 손익계산서 (표)", "code", "파일")),
        S("extract_tables", f"표 {len(tb)} 개를 찾았다. 리스트의 리스트로 나온다.",
          TX(str(ns["found"][0][:4]).replace("], [", "],\n ["), "out", "found[0][:4]")),
        S("DataFrame", "첫 줄을 열 이름으로 올리면 엑셀에서 읽은 것과 같은 모양이다. 5장의 정리 도구를 그대로 쓸 수 있다.",
          T(tb[0].head(8), title="tables[0]"), T(tb[1].head(5), title="tables[1]")),
    ]
