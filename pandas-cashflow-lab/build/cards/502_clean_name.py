from lib import *
from snippets import RAW

CARD = dict(
    id="clean_name", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd='str.replace(r"...", "", regex=True)',
    title="계정 이름에서 번호와 주석을 떼어 낸다", excel="찾기 및 바꾸기, TRIM",
    desc='공시의 계정 이름에는 "Ⅱ. 매출채권 (주석3)" 처럼 앞 번호와 주석 번호가 붙고, "과 목" 처럼 글자 사이에 공백도 있다. '
         "이름이 한 글자라도 다르면 뒤에서 계정을 찾지 못한다. str.replace 에 정규식을 주어 주석 괄호, 앞 번호, 공백을 차례로 지운다. "
         "정규식에서 ^ 는 맨 앞, \\s 는 공백, [ ] 는 그 안의 글자 중 하나, + 는 한 번 이상을 뜻한다.",
    code=RAW + r'''

name = raw_bs["과 목"]
name = name.str.replace(r"\(주석[^)]*\)", "", regex=True)                    # (주석3) 지우기
name = name.str.replace(r"^\s*[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ0-9]+\s*[.)]\s*", "", regex=True)   # 앞 번호 지우기
name = name.str.replace(" ", "")                                            # 공백 지우기
print(pd.DataFrame({"before": raw_bs["과 목"], "after": name}))''',
    tip="회사마다 번호 모양이 다르다. (1), 가., ① 같은 번호가 나오면 [ ] 안에 그 글자를 더한다. 지운 뒤에는 name.unique() 로 이름 목록을 눈으로 한 번 본다.",
    talk=[dict(who="fly", text='"매출채권 (주석3)" 과 "매출채권" 은 컴퓨터한테 다른 이름이야.')],
)

def stages(ns, out):
    import pandas as pd
    raw, name = ns["raw_bs"]["과 목"], ns["name"]
    t = pd.DataFrame({"before": raw.str.replace(" ", "␣"), "after": name})
    ch = [i for i in range(len(t)) if raw[i] != name[i]]
    return [
        S("원본 이름", "앞 번호, 주석 번호, 들여쓰기 공백(␣)이 붙어 있다.", T(t[["before"]])),
        S("정규식으로 지우기", "세 번의 replace 를 거치면 계정 이름만 남는다.", T(t, hl=("after",), hlrows=ch)),
    ]
