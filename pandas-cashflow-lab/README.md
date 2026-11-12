# pandas 로 만드는 현금흐름표

**손익계산서·재무상태표에서 간접법으로, 생성AI 앱까지 37장** · 글 · 안상선 ((주)M-Robo 대표) · 파이썬과 회계데이터 분석

손익계산서와 재무상태표(기초·기말)로 간접법 현금흐름표를 pandas 코드 한 줄씩 만들고, 엑셀·PDF 를 읽어 자동으로 현금흐름표로 바꾸는 앱까지 만드는 한 페이지 책입니다. 카드마다 표가 움직이는 그림, Colab 에 그대로 붙여 넣는 코드, 실제 실행 결과가 있습니다. 표지에 **앱을 만드는 일곱 걸음**과 **과제 안내**가 있어 학생 과제 안내서로도 씁니다.

형식은 [보면서 배우는 pandas](https://adminmrobo.github.io/learn-pandas-visually_korean/) 와 같고, 예제와 원칙은 [현금흐름표 연구실](https://adminmrobo.github.io/cashflow-lab/) 의 (주)SG화학 2014년 숫자(순이익 170 → 영업현금 270, 투자 −500, 재무 +380, 현금 250 → 400)를 씁니다.

| 장 | 내용 | 카드 |
|---|---|---|
| 0 | 한눈에 보는 간접법 | 1 |
| 1 | 재무제표를 표로 담기 (Series, DataFrame, 대차 확인, 증감) | 4 |
| 2 | 영업활동: 간접법 다섯 계단 | 5 |
| 3 | 투자·재무활동 (취득, 처분, 차입금, 배당 역산) | 4 |
| 4 | 조립하고 검산하기 (concat, 검산, 소계, 폭포 차트) | 4 |
| 5 | 엑셀·PDF 에서 숫자 꺼내기 (read_excel, 정규식, ffill, pdfplumber) | 7 |
| 6 | 생성AI 에게 맡기기 (프롬프트, API, JSON, 검사) | 5 |
| 7 | 앱으로 만들기 (make_cashflow, Streamlit, 실행, 내려받기, 키 보관) | 5 |
| 8 | 과제 안내 (제출물·배점, 공시 대조표) | 2 |

카드마다 주소가 있습니다: `.../#cfo`, `.../#engine`, `.../#homework`

## 저장소 구조

```
index.html                 ← 책 (build 가 만든다)
app/app.py                 ← 현금흐름표 자동 작성 앱 (Streamlit). 7장 app_write 카드의 코드와 같은 파일
app/requirements.txt
data/sg_2014.xlsx, .pdf    ← 연습 파일 (공시처럼 소계·쉼표·괄호가 섞인 모양)
code/prompt_extract.md     ← 생성AI 프롬프트
docs/ASSIGNMENT.md         ← 과제 안내 (표지의 HOMEWORK 와 같은 내용)
docs/IMG_prompts.md        ← 대표 그림 제작 지시문
assets/chars, hero, img    ← 캐릭터, 대표 그림, 차트
build/                     ← 다시 만드는 도구 (cards/ 카드 37개, snippets.py 공통 자료·함수, cover.html 표지)
```

## 앱 실행

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

왼쪽에서 '연습 자료(SG화학 2014)로 해 보기' 를 켜면 영업 270, 투자 −500, 재무 380, 현금의 증가 150 이 나오고 검산 넷을 통과합니다. `data/sg_2014.xlsx`, `data/sg_2014.pdf` 를 올려도 같은 결과가 나옵니다. '생성AI' 방법은 Google AI Studio 의 API 키가 필요하고, 모델 이름은 왼쪽 칸에서 바꿉니다.

## 고치고 다시 만들기

```bash
pip install -r build/requirements.txt
python build/make_app.py         # app/app.py, data/ 연습 파일
python build/build.py            # 모든 카드 실행 → index.html, assets/img
python build/build.py cfo        # 카드 하나만 시험 (build/_preview/cfo.json)
```

카드 코드를 실제로 실행해 출력과 그림을 만들기 때문에 페이지의 숫자는 코드 결과와 같습니다. 생성AI 카드(6장)는 API 를 부르지 않고 `build/snippets.py` 의 예시 응답으로 실행합니다. 표지 글은 `build/cover.html` 을 고친 뒤 `python build/patch_template.py build/base_shell.html build/template.html` (build 폴더 안에서 실행)로 틀에 넣습니다.

## GitHub Pages

`index.html` 이 저장소 맨 위에 있게 올리고, Settings → Pages → Deploy from a branch → `main` / `(root)`.

---
제작 안상선 (Ahn, Sang-Sun) · sangsun.ahn@gmail.com · © 2026 All rights reserved.
예제는 (주)SG화학 2014년 강의용 숫자입니다. 교육용 자료이며 세무·회계·투자 자문이 아닙니다. 주판봇은 연구실 캐릭터이며, 극 중 대사는 비유일 뿐 투자 권유가 아닙니다.
