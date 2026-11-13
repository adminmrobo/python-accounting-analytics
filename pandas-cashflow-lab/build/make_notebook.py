"""index.html 의 카드에서 Colab 실습 노트북과 한 셀 코드를 만든다.  usage: python build/make_notebook.py  (build.py 다음에)
- colab/pandas_cashflow_lab.ipynb : 5~10장 카드 = 셀 하나씩 (설명 + 코드)
- colab/all_in_one.py             : 11장 한 셀로 끝내기 코드"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://adminmrobo.github.io/python-accounting-analytics/pandas-cashflow-lab/"
h = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
i = h.find('<script id="data"'); j = h.find("</script>", i)
cards = json.loads(h[h.find(">", i) + 1:j].replace("<\\/", "</"))
md = lambda s: {"cell_type": "markdown", "metadata": {}, "source": s.splitlines(True)}
code = lambda s: {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": s.splitlines(True)}
cells = [md(f"""# pandas 로 만드는 현금흐름표 · 실습 노트북

글 · 안상선 ((주)M-Robo 대표) · 파이썬과 회계데이터 분석

1. [재무제표 생성기]({BASE}generator.html)에 **내 학번**을 넣고 `재무제표_학번.csv` 를 내려받는다. 화면의 **확인 코드**를 적어 둔다.
2. 아래 셀을 **위에서부터 차례로** 실행한다 (Shift+Enter). 첫 셀에서 '파일 선택' 단추가 나오면 받은 CSV 를 고른다.
3. 현금흐름표 · 차트 · 재무비율이 나오고, 결과 파일 다섯 개가 내려받아진다.
4. 10장 첫 셀의 출력 전체를 복사해 생성AI 채팅창에 붙여 넣으면 분석보고서가 나온다. 마지막 셀의 검증표로 숫자를 맞춰 본다.

코드는 들여쓰기 · def · for 없이 썼다. 줄마다의 뜻과 엑셀로 하는 방법은 [책의 카드]({BASE}index.html#upload)에 있다.""")]
for c in cards:
    if not ("5." <= c["ch"][:2] or c["ch"][:3] in ("10.",)):
        continue
    if c["id"] in ("all_in_one", "hw_task", "hw_check") or not c["ch"][0].isdigit():
        continue
    n = int(c["ch"].split(".")[0])
    if n < 5 or n > 10:
        continue
    cells.append(md(f"## {c['ch']} · {c['title']}\n\n{c['desc']}\n\n책의 카드: [{c['id']}]({BASE}index.html#{c['id']})"))
    cells.append(code(c["code"]))
cells.append(md(f"""## 다음 할 일

- 10장 첫 셀의 출력(또는 내려받은 `보고서프롬프트_학번.txt`)을 **고치지 않고** 생성AI 에 붙여 넣는다.
- 받은 보고서를 `보고서검증_학번.csv` 로 검산하고 고친다.
- 제출물과 배점은 [과제 안내]({BASE}index.html#homework)를 따른다."""))
nb = {"nbformat": 4, "nbformat_minor": 5, "metadata": {"colab": {"provenance": []}, "kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}}, "cells": cells}
os.makedirs(os.path.join(ROOT, "colab"), exist_ok=True)
json.dump(nb, open(os.path.join(ROOT, "colab", "pandas_cashflow_lab.ipynb"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
one = [c for c in cards if c["id"] == "all_in_one"][0]["code"]
open(os.path.join(ROOT, "colab", "all_in_one.py"), "w", encoding="utf-8").write(
    "# pandas 로 만드는 현금흐름표 · 한 셀로 끝내기\n# Colab 새 노트북의 첫 셀에 통째로 붙여 넣고 Shift+Enter → 생성기에서 받은 재무제표_학번.csv 를 고른다.\n\n" + one + "\n")
print("colab/pandas_cashflow_lab.ipynb 셀", len(cells), "개 · colab/all_in_one.py", len(one.splitlines()), "줄")
