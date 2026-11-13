from lib import *
import glob as _glob, os as _os, importlib.util as _ilu

def _chain_code():
    """5~10장 chain 카드의 코드를 차례로 이어 붙인다 (학생에게 보이는 코드는 카드 코드 그대로)."""
    here = _os.path.dirname(_os.path.abspath(__file__))
    out = []
    for p in sorted(_glob.glob(_os.path.join(here, "*.py"))):
        n = _os.path.basename(p)
        if not ("0500" < n[:4] < "1100"):
            continue
        spec = _ilu.spec_from_file_location("_c" + n[:4], p); m = _ilu.module_from_spec(spec); spec.loader.exec_module(m)
        out.append(f"# ── {m.CARD['ch'].split('. ')[0]}장 · {m.CARD['title']} ──\n" + m.CARD["code"])
    return out

PARTS = _chain_code()

CARD = dict(
    id="all_in_one", ch="11. 한 셀로 끝내기", cmd="5~10장 코드를 한 셀에", session=True,
    title="복사 한 번, 실행 한 번: 올리기부터 보고서 프롬프트까지", excel="엑셀 검산 파일 한 권 (재무제표 → 현금흐름표 → 재무비율)",
    desc="5~10장 카드의 코드를 순서대로 이어 붙인 것이다. Colab 새 노트북의 첫 셀에 통째로 붙여 넣고 Shift+Enter 를 누르면 '파일 선택' 단추가 나온다. "
         "생성기에서 받은 재무제표_학번.csv 를 고르면 현금흐름표, 차이 원인, 차트, 재무비율, 저장·내려받기, 생성AI 프롬프트가 한 번에 나온다. "
         "내려받는 파일은 다섯 개다: 현금흐름표_학번.csv, 재무비율_학번.csv, 차트_학번.png, 보고서프롬프트_학번.txt, 보고서검증_학번.csv. "
         "들여쓰기·def·for 가 없으니 위에서 아래로 읽으면 무엇을 하는지 그대로 보인다. 어느 줄이 무엇인지는 해당 장의 카드를 펼쳐 본다.",
    code="\n\n".join(PARTS),
    xl=[
        ("# ── 5장 ── (올리기 · 나누기 · 대차)", "내회사_엑셀검산.xlsx 의 '재무제표' 시트에 CSV 내용을 붙여 넣는다. I열(증감)·J열(부호 붙인 금액)이 자동으로 계산된다."),
        ("# ── 6장 ── (현금흐름표 · 차이 원인)", "'현금흐름표' 시트 C2:C21. 검산 칸 C21 이 '통과' 인지 본다."),
        ("# ── 7장 ── (차트 세 장)", "'현금흐름표' 시트 옆에 폭포 차트, '재무제표' 시트 옆에 누적 막대형 차트."),
        ("# ── 8장 ── (재무비율 열세 개 · 판정)", "'재무비율' 시트 C열(값)·G열(판정)."),
        ("# ── 9장 ── (CSV · PNG 저장)", "시트마다 다른 이름으로 저장 → CSV UTF-8, 차트는 그림으로 저장."),
        ("# ── 10장 ── (프롬프트 · 검증표)", "지시서 + 세 표를 메모장에 붙여 생성AI 로. 검증표 시트에 O/X."),
    ],
    tip="중간에 오류가 나면 오류 메시지 위쪽의 '# ── n장' 줄을 찾아 그 장의 카드를 본다. 가장 흔한 원인은 파일을 고르지 않고 취소한 경우(list(up)[0] 에서 IndexError)와, 생성기에서 받은 CSV 의 열 이름을 엑셀에서 고쳐 저장한 경우다. 같은 코드가 저장소의 colab/all_in_one.py 와 실습 노트북 colab/pandas_cashflow_lab.ipynb 에 있다.",
    talk=[
        dict(who="robo", state="success", text="삐빅! 셀 하나로 표·차트·비율·프롬프트 완성."),
        dict(who="x", text="(방청석의 X1 · X2 · X3 가 조용히 박수를 친다)"),
    ],
)

def stages(ns, out):
    import pandas as pd
    t = pd.DataFrame({"순서": [p.splitlines()[0].replace("# ── ", "").replace(" ──", "") for p in PARTS],
                      "줄 수": [len(p.splitlines()) for p in PARTS]})
    files = pd.DataFrame({"내려받는 파일": [f"현금흐름표_{ns['sid']}.csv", f"재무비율_{ns['sid']}.csv", f"차트_{ns['sid']}.png", f"보고서프롬프트_{ns['sid']}.txt", f"보고서검증_{ns['sid']}.csv"],
                          "쓰는 곳": ["보고서 표", "보고서 표", "보고서 그림", "생성AI 채팅창", "과제 제출 (검증표)"]})
    return [
        S("이어 붙인 순서", f"카드 {len(PARTS)} 장의 코드, 모두 {sum(t['줄 수'])} 줄.", T(t)),
        S("결과 파일", "한 번 실행으로 다섯 개가 내려받아진다.", T(files)),
        S("한 장 요약", "9장의 그림이 함께 나온다.", IMG("all_in_one", 4)),
    ]
