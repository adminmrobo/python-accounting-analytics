# pandas 로 만드는 현금흐름표

**손익계산서·재무상태표에서 간접법으로, 학번별 회사 분석보고서까지 36장** · 글 · 안상선 ((주)M-Robo 대표) · 파이썬과 회계데이터 분석

손익계산서와 재무상태표(기초·기말)로 간접법 현금흐름표를 pandas 코드 한 줄씩 만드는 한 페이지 책입니다. 카드마다 표가 움직이는 그림, Colab 에 그대로 붙여 넣는 코드, 실제 실행 결과, **엑셀로 따라 하기 표**가 있습니다. 표지에 **실습 여섯 걸음**과 **과제 안내**가 있어 학생 과제 안내서로도 씁니다.

- 0~4장: (주)SG화학 2014년 숫자로 간접법을 익힌다 (순이익 170 → 영업현금 270, 투자 −500, 재무 +380, 현금 250 → 400)
- 5~10장: **학번으로 만든 나만의 회사**. 생성기에서 받은 CSV 를 Colab 에 올려 현금흐름표·차트·재무비율을 만들고 CSV·PNG 로 저장한 뒤, 정해진 프롬프트로 생성AI 분석보고서를 받아 검산한다
- 11~12장: 한 셀로 끝내기, 과제 안내

**코드 규칙:** pandas · numpy · matplotlib 만 씁니다. 들여쓰기 없음 · `def` 없음 · `for` 없음. 위에서 아래로 한 줄이 한 동작입니다. 빌드가 이 규칙을 검사합니다. 코드의 모든 줄은 엑셀 동작이나 수식으로 설명할 수 있게 썼고, 같은 계산을 수식으로 넣은 통합 문서 두 권이 있습니다.

형식은 [보면서 배우는 pandas](https://adminmrobo.github.io/learn-pandas-visually_korean/) 와 같고, 내용은 [현금흐름표 연구실](https://adminmrobo.github.io/cashflow-lab/) 을 따릅니다.

| 장 | 내용 | 카드 |
|---|---|---|
| 0 | 한눈에 보는 간접법 | 1 |
| 1 | 재무제표를 표로 담기 (Series, DataFrame, 대차 확인, 증감) | 4 |
| 2 | 영업활동: 간접법 다섯 계단 | 5 |
| 3 | 투자·재무활동 (취득, 처분, 차입금, 배당 역산) | 4 |
| 4 | 조립하고 검산하기 (concat, 검산, 소계, 폭포 차트) | 4 |
| 5 | 내 재무제표 불러오기 (files.upload, 나누기, 대차와 '이익 vs 현금') | 3 |
| 6 | 내 회사의 현금흐름표 (계단 그대로, 차이 원인 큰 세 줄) | 2 |
| 7 | 차트로 보기 (재무상태표 구조, 순이익 → 영업현금 폭포, 현금 다리) | 3 |
| 8 | 주요 재무비율 (재료, 비율 열세 개, 양호·주의 판정) | 3 |
| 9 | 저장하고 내려받기 (CSV, PNG) | 2 |
| 10 | 생성AI 로 분석보고서 (정해진 프롬프트, 검증표) | 2 |
| 11 | 한 셀로 끝내기 | 1 |
| 12 | 과제 안내 (제출물·배점, 제출 전 점검표) | 2 |

카드마다 주소가 있습니다: `.../#cfo`, `.../#upload`, `.../#all_in_one`, `.../#homework`

## 학생이 하는 일

1. `generator.html` 에 학번을 넣고 `재무제표_학번.csv` 와 확인 코드를 받는다 (같은 학번은 언제나 같은 숫자).
2. Colab 에서 `colab/pandas_cashflow_lab.ipynb` 를 열거나, 새 노트북에 `colab/all_in_one.py` 를 붙여 넣고 실행 → CSV 를 고른다.
3. 현금흐름표·차트·재무비율이 나오고 `현금흐름표_학번.csv`, `재무비율_학번.csv`, `차트_학번.png`, `보고서프롬프트_학번.txt`, `보고서검증_학번.csv` 가 내려받아진다.
4. 보고서프롬프트를 생성AI 에 붙여 넣어 분석보고서를 받고, 검증표로 숫자를 맞춰 고친다.

Colab 에서 노트북 바로 열기: https://colab.research.google.com/github/adminmrobo/python-accounting-analytics/blob/main/pandas-cashflow-lab/colab/pandas_cashflow_lab.ipynb

## 저장소 구조

```
index.html                    ← 책 (build 가 만든다)
generator.html                ← 학번 → 가상 회사 재무제표 CSV 생성기 (대차·현금 항등식이 정확히 맞게 정수로 만든다)
colab/pandas_cashflow_lab.ipynb ← 5~10장 카드를 셀로 옮긴 실습 노트북
colab/all_in_one.py           ← 한 셀로 끝내기 코드
data/cashflow_by_excel.xlsx   ← 0~4장 SG화학 계산을 엑셀 수식으로
data/내회사_엑셀검산.xlsx      ← 5~8장 계산을 엑셀 수식으로 ('재무제표' 시트에 내 CSV 를 붙여 넣으면 다시 계산)
docs/ASSIGNMENT.md            ← 과제 안내 (표지의 HOMEWORK 와 같은 내용)
docs/IMG_prompts.md           ← 대표 그림 제작 지시문 (아홉 식구 전원)
assets/chars, hero, img       ← 캐릭터, 대표 그림(임시), 차트
build/                        ← 다시 만드는 도구 (cards/ 카드 36개, snippets.py, cover.html 표지, CARDS_GUIDE.md 규칙)
```

## 고치고 다시 만들기

```bash
pip install -r build/requirements.txt        # node 도 필요하다 (생성기 코드를 그대로 돌려 표본 CSV 를 만든다)
python build/build.py            # 모든 카드 실행 → index.html, assets/img/*.png
python build/make_excel.py       # data/ 엑셀 통합 문서 두 권
python build/make_notebook.py    # colab/ 노트북과 한 셀 코드 (build.py 다음에)
python build/make_docs.py        # docs/ASSIGNMENT.md
node build/gen_sample.js --check # 학번 3,000개로 대차·현금 항등식 검사
```

카드 코드를 실제로 실행해 출력과 그림을 만들기 때문에 페이지의 숫자는 코드 결과와 같습니다. 5~10장 카드는 Colab 노트북처럼 한 이름공간에서 차례로 실행되고, `files.upload()` 는 표본 학번 20261005 의 CSV(생성기와 같은 코드로 만든 것)를 올린 것처럼 동작합니다. 카드 코드가 규칙(들여쓰기·def·for 없음)을 어기거나 엑셀 설명이 없으면 빌드가 멈춥니다. 표지 글은 `build/cover.html` 을 고친 뒤 build 폴더에서 `python patch_template.py base_shell.html template.html` 로 틀에 넣습니다.

---
제작 안상선 (Ahn, Sang-Sun) · sangsun.ahn@gmail.com · © 2026 All rights reserved.
0~4장은 (주)SG화학 2014년 강의용 숫자, 5장부터는 학번으로 만든 가상 회사입니다. 교육용이며 세무·회계·투자 자문이 아닙니다. 주판봇은 연구실 캐릭터이며, 극 중 대사는 비유일 뿐 투자 권유가 아닙니다.
