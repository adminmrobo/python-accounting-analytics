from lib import *
from snippets import REPORT

CARD = dict(
    id="ai_prompt", ch="10. 생성AI 로 분석보고서", cmd="REPORT + to_csv() → print", chain=True,
    title="정해진 프롬프트에 내 숫자를 붙여 한 덩어리로 출력한다", excel="지시서 아래에 세 표를 붙여 넣은 메모",
    desc="생성AI 에게는 계산을 시키지 않는다. 계산은 이미 pandas 가 끝냈다. 생성AI 는 그 숫자를 읽고 글로 풀어 쓰는 일만 한다. "
         "정해진 프롬프트(REPORT) 뒤에 회사 정보, 원래 재무제표, 현금흐름표, 재무비율을 to_csv 로 글자로 바꿔 붙인다. "
         "출력된 글 전체를 복사해 생성AI(ChatGPT, Claude, Gemini 등 아무 채팅창)에 붙여 넣으면 분석보고서가 나온다. "
         "같은 글을 txt 파일로도 저장해 내려받는다. 아래 출력은 표본 학번의 앞부분과 끝부분이다.",
    code=REPORT + '''

info = f"회사명: {company} (학번 {sid} 로 만든 가상 회사), 단위: 백만원, 회계기간: 1년\\n"
statements = fs[["표", "구분", "세부", "계정과목", "기초", "기말"]].to_csv(index=False)
cf_text = cf.to_csv(index=False)
ratio_text = ratio[["분류", "비율", "값", "단위", "계산식", "기준", "방향", "판정"]].to_csv(index=False)
prompt = REPORT + "[회사]\\n" + info + "\\n[재무제표]\\n" + statements + "\\n[현금흐름표 (간접법)]\\n" + cf_text + "\\n[재무비율]\\n" + ratio_text
print(prompt)                                          # ← 이 출력 전체를 복사해 생성AI 에 붙여 넣는다

prompt_name = f"보고서프롬프트_{sid}.txt"
f = open(prompt_name, "w", encoding="utf-8")
f.write(prompt)
f.close()
files.download(prompt_name)''',
    xl=[
        ("REPORT = \"\"\"...\"\"\"", "메모장 맨 위에 정해진 지시서(REPORT)를 붙여 넣는다."),
        ("info = f\"회사명: {company} …\"", '=B2 & " (학번 " & A2 & " 로 만든 가상 회사)" 처럼 & 로 글을 잇는다.'),
        ('fs[[...]].to_csv(index=False)', "재무제표 CSV 를 메모장으로 열어 전체 복사 → 지시서 아래에 붙여 넣기."),
        ("cf.to_csv · ratio.to_csv", "9장에서 저장한 현금흐름표_학번.csv, 재무비율_학번.csv 도 같은 방법으로 붙여 넣는다."),
        ("print(prompt)", "완성된 메모 전체를 선택(Ctrl+A) → 복사(Ctrl+C) → 생성AI 채팅창에 붙여 넣기(Ctrl+V)."),
        ("open(...) · f.write · f.close · files.download", "메모를 보고서프롬프트_학번.txt 로 저장한다."),
    ],
    tip="출력이 길어 Colab 이 일부를 접으면, 내려받은 txt 파일을 열어 전체를 복사한다. 생성AI 에 파일을 올릴 수 있으면 txt 와 9장의 CSV·PNG 를 함께 올려도 된다. 프롬프트는 바꾸지 말고 그대로 쓴다. 바꾸고 싶은 점은 과제 보고서의 '내 의견' 에 적는다.",
    talk=[
        dict(who="asst", text="AI 가 계산까지 해 주면 안 돼요?"),
        dict(who="doc", text="계산은 우리가 끝냈어요. AI 는 글로 풀어 쓰고, 우리는 그 글을 검산해요."),
    ],
)

def stages(ns, out):
    P = ns["REPORT"]
    p = ns["prompt"]
    return [
        S("정해진 프롬프트", "지킬 것 다섯 가지와 보고서 구성 아홉 칸.",
          TX(P[:P.index("[보고서 구성]")].strip(), "code", "REPORT 앞부분")),
        S("보고서 구성", "생성AI 가 이 순서로 쓴다.", TX(P[P.index("[보고서 구성]"):P.index("[자료]")].strip(), "code", "REPORT 가운데")),
        S("내 숫자 붙이기", f"회사 정보와 세 표를 글자로 붙였다. 전체 {len(p)} 글자. 이것을 복사해 생성AI 에 붙여 넣는다.",
          TX(p[p.index("[회사]"):p.index("[회사]") + 420] + "\n…\n" + p[-260:], "out", "prompt 의 [자료] 부분")),
    ]
