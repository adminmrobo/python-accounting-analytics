from lib import *

CARD = dict(
    id="excel_out", ch="7. 앱으로 만들기", cmd="pd.ExcelWriter(io.BytesIO())",
    title="결과를 시트 여러 장짜리 엑셀로 내려받게 한다", excel="다른 이름으로 저장",
    desc="앱은 서버에서 돌기 때문에 파일을 디스크에 저장해도 사용자가 가져갈 수 없다. 메모리 안의 가짜 파일(io.BytesIO)에 엑셀을 쓰고, "
         "그 내용(bytes)을 st.download_button 에 넘긴다. ExcelWriter 를 with 로 열고 to_excel 을 여러 번 부르면 시트가 여러 장 생긴다. "
         "현금흐름표뿐 아니라 검산표와 정리된 원본까지 넣어, 받은 사람이 숫자의 출처를 따라갈 수 있게 한다.",
    code='''import io
import pandas as pd

cf = pd.DataFrame({"활동": ["영업활동", "투자활동", "재무활동"], "항목": ["합계", "합계", "합계"], "금액": [270, -500, 380]})
checks = pd.DataFrame({"검산": ["C 세 활동 합계 = 현금 증감"], "계산값": [150], "기준값": [150], "통과": [True]})

buf = io.BytesIO()                                   # 메모리 안의 파일
with pd.ExcelWriter(buf) as w:
    cf.to_excel(w, sheet_name="현금흐름표", index=False)
    checks.to_excel(w, sheet_name="검산", index=False)
data = buf.getvalue()
print(type(data), len(data), "bytes")
# 앱에서는:  st.download_button("엑셀로 내려받기", data, "cashflow.xlsx")

back = pd.read_excel(io.BytesIO(data), sheet_name=None)     # 제대로 써졌는지 다시 읽어 본다
print(list(back))
print(back["현금흐름표"])''',
    tip="Colab 에서 파일로 받고 싶으면 open(\"cashflow.xlsx\", \"wb\").write(data) 로 저장한 뒤 왼쪽 폴더에서 내려받는다.",
)

def stages(ns, out):
    return [
        S("표 두 장", "현금흐름표와 검산표.", T(ns["cf"], title="cf"), T(ns["checks"], title="checks")),
        S("BytesIO 에 쓰기", f"디스크가 아니라 메모리에 엑셀이 만들어진다. {len(ns['data'])} bytes.",
          TX("cashflow.xlsx (메모리)\n ├ 현금흐름표\n └ 검산", "code", "buf"), links=[[0, 0], [1, 0]]),
        S("다시 읽기", "시트 두 장이 그대로 들어 있다.", T(ns["back"]["현금흐름표"], title='back["현금흐름표"]')),
    ]
