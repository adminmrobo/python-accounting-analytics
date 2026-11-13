# 카드 작성 규칙 (pandas 로 만드는 현금흐름표)

- 파일: `build/cards/NNNN_<id>.py` (NNNN = 장번호×100 + 순서, 네 자리). `CARD = dict(id, ch, cmd, title, excel, desc, code, xl, tip, talk)` 와 `stages(ns, out)`.
- **코드 규칙 (build.py 가 검사하고, 어기면 빌드가 멈춘다)**
  1. 들여쓰기 없음. 모든 줄이 첫 칸에서 시작한다. 긴 목록은 괄호 안에서 줄을 바꾸되 다음 줄도 첫 칸에서 시작한다.
  2. `def` 없음 (`lambda`, `class` 도 없음).
  3. `for` 없음 (`while`, 리스트 컴프리헨션도 없음). `if`·`with`·`try` 블록도 쓰지 않는다. 한 줄짜리 `A if 조건 else B` 는 엑셀의 IF 와 같아 허용한다.
  - 한 줄이 한 동작이고, 변수에 담아 다음 줄로 넘긴다. 반복은 열 연산(str.replace, where, merge, groupby)으로 한다.
  - 파일은 `w = pd.ExcelWriter(...)` … `w.close()`, `f = open(...)` … `f.close()` 처럼 열고 닫는다.
- **엑셀 설명 (xl, 필수)**: `[(파이썬 코드, 엑셀로 하면), ...]`. 코드의 모든 동작을 엑셀 동작이나 수식으로 옮긴다. 셀 주소는 0~4장은 `data/cashflow_by_excel.xlsx`, 5~10장은 `data/내회사_엑셀검산.xlsx` (build/make_excel.py 가 만든다)의 시트·셀과 맞춘다. 생성기 CSV 를 엑셀로 열면 2~13행 재무상태표, 14~21행 손익계산서, G열 기초, H열 기말이다.
- 자료: 0~4장은 `build/snippets.py` 의 DATA · DATA_D · CF_PARTS 문자열을 붙여 쓴다 ((주)SG화학 2014년, 카드마다 혼자 돈다).
- 5~10장은 `chain=True`: Colab 노트북처럼 한 이름공간에서 카드 순서대로 실행된다. 앞 카드의 변수(fs, bs, b, d, pl, ni, cf, total, ratio …)를 그대로 쓴다. `files.upload()` 는 표본 학번(build.py 의 SAMPLE_ID)의 CSV 를 올린다. 11장 all_in_one 은 5~10장 코드를 이어 붙여 만든다.
- 생성기(`generator.html`)의 계정과목 이름·순서·열(학번, 회사명, 표, 구분, 세부, 계정과목, 기초, 기말)을 바꾸면 5~10장 카드, `make_excel.py` 의 셀 주소, 엑셀 설명을 함께 고친다.
- 차트 글자는 영어(Colab 한글 깨짐 방지). 설명·caption·talk 는 한국어, 문체는 "~다." 평서문. '장부' 라는 말은 쓰지 않는다.
- stages 의 숫자와 caption 의 숫자는 ns 의 실제 값에서 꺼낸다 (stages 함수 안에서는 파이썬을 자유롭게 써도 된다. 학생에게 보이는 코드가 아니다).
- talk who: doc(박사) · asst(조수) · fly(초파리) · robo(주판봇, state=idle|thinking|wrong|confused|success) · sia(시아, 판정) · moa(모아, 기록) · x(방청석 X1~X3, 대사 대신 지문). 최대 2줄.
- 생성AI 는 파이썬에서 부르지 않는다. 10장은 정해진 프롬프트(snippets.REPORT)에 숫자를 붙여 출력하고, 학생이 채팅창에 붙여 넣는다.
