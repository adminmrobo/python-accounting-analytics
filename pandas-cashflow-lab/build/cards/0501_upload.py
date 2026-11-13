from lib import *

CARD = dict(
    id="upload", ch="5. 내 재무제표 불러오기", cmd="files.upload() → pd.read_csv()", chain=True,
    title="학번으로 만든 CSV 를 Colab 에 올려 읽는다", excel="파일 → 열기 (CSV)",
    desc="0~4장은 (주)SG화학 숫자를 코드에 직접 적었다. 5장부터는 나만의 회사다. 먼저 생성기(generator.html)에 학번을 넣어 재무제표_학번.csv 를 받는다. "
         "같은 학번은 언제나 같은 숫자가 나오고, 학번마다 회사와 숫자가 다르다. "
         "Colab 에서는 google.colab 의 files.upload() 를 실행하면 '파일 선택' 단추가 나온다. 받은 CSV 를 고르면 Colab 폴더에 올라가고, 올린 파일 이름이 사전의 키로 돌아온다. "
         "list(up)[0] 로 그 이름을 꺼내 pd.read_csv 로 읽는다. 이 카드부터 12장 전까지는 하나의 노트북에서 차례로 실행한다. 앞 셀에서 만든 변수를 다음 셀이 그대로 쓴다.",
    code='''import numpy as np
import pandas as pd
from google.colab import files
pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄 맞춤

up = files.upload()                  # '파일 선택' 단추를 눌러 재무제표_학번.csv 를 고른다
name = list(up)[0]                   # 올린 파일 이름
fs = pd.read_csv(name)               # CSV → 표
company = fs["회사명"].iloc[0]
sid = str(fs["학번"].iloc[0])
print("회사:", company, "| 학번:", sid, "| 줄 수:", len(fs))
print(fs[["표", "구분", "세부", "계정과목", "기초", "기말"]])''',
    xl=[
        ("files.upload()", "생성기에서 받은 재무제표_학번.csv 를 더블클릭해 엑셀로 연다. (Colab 에서는 파일을 Colab 폴더로 올리는 일)"),
        ("name = list(up)[0]", "엑셀 창 맨 위에 보이는 파일 이름."),
        ("fs = pd.read_csv(name)", "열린 시트 전체. A 학번 · B 회사명 · C 표 · D 구분 · E 세부 · F 계정과목 · G 기초 · H 기말, 2~13행 재무상태표, 14~21행 손익계산서."),
        ('fs["회사명"].iloc[0]', "B2 셀"),
        ("len(fs)", "=COUNTA(F2:F21) → 20"),
    ],
    tip="파일을 고치면 다시 올리기 전에 Colab 왼쪽 폴더에서 옛 파일을 지운다. 같은 이름이 있으면 Colab 이 '재무제표_학번 (1).csv' 로 바꿔 올린다. 생성기는 같은 폴더의 generator.html 이다. 학번은 내 것을 쓴다. 다른 사람의 학번을 쓰면 확인 코드가 달라 과제에서 바로 드러난다.",
    talk=[
        dict(who="moa", text="학번마다 회사가 달라요. 표본 학번 20261005 는 (주)은하유통이에요."),
        dict(who="doc", text="숫자가 다 다르니 보고서도 다 달라야 해요."),
    ],
)

def stages(ns, out):
    fs = ns["fs"]
    v = fs[["표", "구분", "세부", "계정과목", "기초", "기말"]].astype(object).fillna("")
    return [
        S("생성기", f"학번 {ns['sid']} 을 넣으면 {ns['company']} 의 재무제표가 만들어진다. 같은 학번은 언제나 같은 숫자다.",
          TX(f"generator.html\n 학번: {ns['sid']}\n → 재무제표_{ns['sid']}.csv", "code", "생성기")),
        S("upload", "files.upload() 가 파일을 Colab 폴더에 올리고 이름을 돌려준다.", TX(out.splitlines()[0], "out", "출력")),
        S("read_csv", "한 파일에 재무상태표 12 줄(기초·기말)과 손익계산서 8 줄(기말 칸에 1년 금액)이 들어 있다.",
          T(v, rcls=["g0"] * 7 + ["g1"] * 3 + ["g2"] * 2 + [""] * 8)),
    ]
