from lib import *
from snippets import RAW

CARD = dict(
    id="to_num", ch="5. 엑셀·PDF 에서 숫자 꺼내기", cmd="Series.map(to_num)",
    title="쉼표, 괄호, △ 가 붙은 글자를 숫자로", excel="VALUE, 찾기 및 바꾸기",
    desc='재무제표의 숫자는 "1,600" 처럼 쉼표가 있고, 음수는 "(280)" 이나 "△280" 으로 적는다. 빈칸이나 "-" 는 0 이다. '
         "이 규칙을 함수 to_num 하나에 담고 map 으로 열 전체에 적용한다. map 은 값 하나하나를 함수에 넣어 결과로 바꿔 준다. "
         "괄호를 음수로 바꾸는 것을 빼먹으면 감가상각누계액이 자산을 늘리는 숫자가 되어 대차가 틀어진다.",
    code=RAW + r'''
import re

def to_num(v):
    s = str(v).strip().replace(",", "")           # 쉼표 지우기
    if s in ("", "-", "nan", "None"):
        return 0
    neg = s[0] in "(△-"                            # 괄호·세모·빼기로 시작하면 음수
    n = int(float(re.sub(r"[()△-]", "", s)))
    return -n if neg else n

for v in ["1,600", "(280)", "△30", "-", "2,100"]:
    print(repr(v), "→", to_num(v))

num = raw_bs["당기말"].map(to_num)
print(pd.DataFrame({"before": raw_bs["당기말"], "after": num}).iloc[4:9])''',
    tip="단위가 천원·백만원인 공시가 많다. 표 위의 '(단위: 천원)' 을 확인하고, 필요하면 num * 1000 으로 원 단위로 맞춘다. 단위를 섞으면 검산은 통과해도 공시와 대조할 때 틀린다.",
    talk=[dict(who="robo", state="confused", text="삐빅? (280) 을 280 으로 읽으면 자산이 560 이나 늘어난다.")],
)

def stages(ns, out):
    import pandas as pd
    raw = ns["raw_bs"]
    t = pd.DataFrame({"과목": raw["과 목"].str.strip(), "before": raw["당기말"].fillna("NaN"), "after": ns["num"]}).iloc[1:9]
    return [
        S("글자", "쉼표가 든 1,600 과 괄호로 적은 (280) 이 있다.", T(t[["과목", "before"]], rcls=["", "", "", "", "hr", "hr", "", "hr"])),
        S("to_num", "쉼표는 지우고 괄호는 음수로 바꿨다. (280) → −280.", T(t, hl=("after",), rcls=["", "", "", "", "ok", "ok", "", "ok"])),
    ]
