from lib import *

CARD = dict(
    id="hw_check", ch="12. 과제 안내", cmd="제출 전 점검표",
    title="내기 전에 열 가지를 확인한다", excel="체크리스트 시트에 O/X",
    desc="제출 전에 아래 열 가지를 확인한다. 대부분 Colab 출력이나 내려받은 파일에서 바로 확인할 수 있다. "
         "X 가 하나라도 있으면 해당 장의 카드로 돌아간다. 점검표 자체도 CSV 로 만들어 엑셀에서 O/X 를 채울 수 있게 했다.",
    code='''import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

todo = pd.DataFrame()
todo["확인할 것"] = ["CSV 파일 이름의 학번이 내 학번이다", "대차가 맞는가: True", "세 활동 합계 = 현금 증감: True",
"차이 원인 큰 세 줄을 보고서에 적었다", "차트 PNG 에 내 학번이 보인다", "재무비율 열세 개의 값이 CSV 와 같다",
"보고서 첫 줄에 회사명·학번·확인 코드", "보고서 검증표의 같은가 칸이 모두 O", "기준이 '교육용 참고값' 이라고 밝혔다",
"생성AI 를 쓴 곳과 직접 고친 곳을 구분했다"]
todo["볼 곳"] = ["5장 upload", "5장 mismatch", "6장 why_diff", "6장 why_diff", "9장 save_png", "9장 save_csv",
"생성기 화면", "10장 ai_verify", "8장 ratio_signal", "12장 hw_task"]
todo["O/X"] = ""
print(todo.to_string(index=False))
todo.to_csv("제출점검표.csv", index=False, encoding="utf-8-sig")''',
    xl=[
        ('todo["확인할 것"], todo["볼 곳"]', "체크리스트 시트 A열·B열"),
        ('todo["O/X"] = ""', "C열을 비워 두고 하나씩 O/X 를 적는다. =COUNTIF(C2:C11, \"X\") 가 0 이면 제출."),
        ('todo.to_csv("제출점검표.csv", …)', "다른 이름으로 저장 → CSV UTF-8"),
    ],
    talk=[dict(who="sia", text="판정. X 가 0 개일 때만 제출입니다.")],
)

def stages(ns, out):
    t = ns["todo"]
    return [S("점검표", "열 가지. 볼 곳을 따라가면 카드로 돌아간다.", T(t[["확인할 것", "볼 곳"]]))]
