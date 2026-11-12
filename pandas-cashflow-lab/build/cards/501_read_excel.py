from lib import *
from snippets import RAW

CARD = dict(
    id="read_excel", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd="pd.read_excel(sheet_name=None, dtype=str)",
    title="엑셀 파일의 모든 시트를 한 번에 읽기", excel="파일 열기",
    desc="지금까지는 숫자를 코드에 직접 적었다. 이제 파일에서 읽는다. 연습용으로 실제 공시처럼 생긴 엑셀 파일을 먼저 만든다. "
         "소계와 총계, 로마 숫자, 주석 번호, 쉼표와 괄호가 섞여 있다. sheet_name=None 은 모든 시트를 {시트 이름: 표} 사전으로 돌려주고, "
         "dtype=str 은 모든 칸을 글자 그대로 읽는다. 쉼표나 괄호가 든 숫자를 pandas 가 멋대로 해석하지 않게 하려는 것이다.",
    code=RAW + '''

# 연습용 엑셀 파일 만들기 (시트 두 장)
with pd.ExcelWriter("sg_2014.xlsx") as w:
    raw_pl.to_excel(w, sheet_name="손익계산서", index=False)
    raw_bs.to_excel(w, sheet_name="재무상태표", index=False)

sheets = pd.read_excel("sg_2014.xlsx", sheet_name=None, dtype=str)
print(list(sheets))
bs_raw = sheets["재무상태표"]
print(bs_raw.head(9))
print(bs_raw.dtypes.tolist())''',
    tip='내 파일로 할 때는 Colab 왼쪽 폴더 아이콘에 파일을 끌어다 놓고 pd.read_excel("파일이름.xlsx", sheet_name=None, dtype=str) 로 읽는다. DART 에서는 감사보고서 화면의 다운로드 버튼으로 엑셀과 PDF 를 받을 수 있다.',
    talk=[
        dict(who="asst", text="엑셀에서 읽었는데 1,600 이 숫자가 아니에요. 왜요?"),
        dict(who="doc", text="쉼표가 있어서 글자예요. 일단 글자로 읽고 직접 바꿔 볼까요?"),
    ],
)

def stages(ns, out):
    sh = ns["sheets"]
    return [
        S("엑셀 파일", "시트 두 장짜리 파일 sg_2014.xlsx.", TX("sg_2014.xlsx\n ├ 손익계산서 (14줄)\n └ 재무상태표 (19줄)", "code", "파일")),
        S("시트 사전", "sheet_name=None 이면 시트 이름이 키인 사전이 된다.",
          T(sh["손익계산서"].head(5).fillna("NaN"), title='sheets["손익계산서"] 앞 5줄'),
          T(sh["재무상태표"].head(9).fillna("NaN"), title='sheets["재무상태표"] 앞 9줄')),
        S("글자로 읽힌 숫자", "자산 줄은 숫자가 비어 NaN, 1,600 과 (280) 은 글자다. 다음 카드부터 하나씩 정리한다.",
          T(sh["재무상태표"].head(9).fillna("NaN"), rcls=["bad", "", "", "", "", "hr", "hr", "", "bad"])),
    ]
