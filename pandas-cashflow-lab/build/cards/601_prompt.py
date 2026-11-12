from lib import *
from snippets import RAW, PROMPT

CARD = dict(
    id="prompt", ch="6. 생성AI 에게 맡기기", cmd="PROMPT + 표.to_csv()",
    title="규칙, 출력 형식, 자료 세 부분으로 프롬프트 만들기", excel="(해당 없음) 사람에게 주는 작업 지시서",
    desc="5장의 정리 도구는 연습 파일과 같은 양식만 읽는다. 회사마다 양식과 계정 이름이 달라서 규칙을 끝없이 고쳐야 한다. "
         "이 부분을 생성AI 에게 맡긴다. 프롬프트는 세 부분이다. 지킬 규칙(부호, 소계 제외, 분류 이름), 답의 형식(JSON 틀), 자료(표를 글자로 바꾼 것). "
         "AI 에게는 읽기와 분류만 시키고 계산은 시키지 않는다. 계산은 pandas 가 하고, 답이 맞는지는 검산이 판정한다. "
         "to_csv 는 표를 쉼표로 나눈 글자로 바꿔 준다.",
    code=RAW + "\n\n" + PROMPT + '''

text = raw_bs.to_csv(index=False) + "\\n" + raw_pl.to_csv(index=False)
prompt = PROMPT + text
print(len(prompt), "글자")
print(prompt[-330:])''',
    tip="규칙 6 '자료에 없는 숫자는 만들지 않는다' 가 중요하다. 생성AI 는 빈칸을 그럴듯한 숫자로 채우는 일이 있다. 그래도 완전히 막을 수는 없어서 6장 뒤쪽의 검사와 7장의 검산이 필요하다.",
    talk=[
        dict(who="asst", text="그냥 '현금흐름표 만들어 줘' 라고 하면 안 돼요?"),
        dict(who="doc", text="그러면 계산까지 AI 가 해요. 읽기만 시키고 계산은 우리가 해요."),
    ],
)

def stages(ns, out):
    P = ns["PROMPT"]
    rule = P[P.index("[규칙]"):P.index("[출력 형식]")].strip()
    form = P[P.index("[출력 형식]"):P.index("[자료]")].strip()
    return [
        S("① 규칙", "부호, 소계 제외, 분류 이름을 번호로 적는다.", TX(rule.replace("다. ", "다.\n   "), "code", "PROMPT 앞부분")),
        S("② 출력 형식", "JSON 틀을 그대로 보여 준다. 열 이름이 5장의 정리된 표와 같다.", TX(form, "code", "PROMPT 가운데")),
        S("③ 자료", f"표를 to_csv 로 글자로 바꿔 끝에 붙인다. 전체 {len(ns['prompt'])} 글자.",
          TX("[자료]\n" + ns["text"][:260] + "…", "out", "PROMPT 끝 + text")),
    ]
