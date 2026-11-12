from lib import *

CARD = dict(
    id="app_run", ch="7. 앱으로 만들기", cmd="streamlit run app.py",
    title="앱을 띄우는 세 가지 방법", excel="(해당 없음) 통합 문서 열기",
    desc="app.py 는 Colab 셀에서 Shift+Enter 로 실행하는 파일이 아니다. 터미널에서 streamlit run app.py 로 띄우면 브라우저에 화면이 열린다. "
         "방법은 셋이다. ① 내 PC: 파이썬을 설치하고 명령 두 줄. 가장 확실하다. ② Streamlit Community Cloud: 깃허브 저장소를 연결하면 주소가 생긴다. 과제 제출용으로 권한다. "
         "③ Colab: 임시 주소를 만들어 주는 터널 프로그램이 필요하고 세션이 끝나면 사라진다. 아래 코드는 설치 목록 파일을 만들고 방법별 명령을 출력한다.",
    code='''# 필요한 라이브러리 목록 파일
with open("requirements.txt", "w") as f:
    f.write("streamlit\\npandas\\nopenpyxl\\npdfplumber\\ngoogle-genai\\n")

local = """[내 PC] 터미널(명령 프롬프트)에서 app.py 가 있는 폴더로 이동한 뒤
  pip install -r requirements.txt
  streamlit run app.py
→ 브라우저에 http://localhost:8501 이 열린다. 끝낼 때는 터미널에서 Ctrl+C"""

cloud = """[Streamlit Community Cloud] share.streamlit.io
  1. 깃허브에 저장소를 만들고 app.py, requirements.txt 를 올린다
  2. share.streamlit.io 에 깃허브 계정으로 로그인 → Create app
  3. 저장소, 브랜치(main), 파일(app.py)을 고르고 Deploy
→ https://<이름>.streamlit.app 주소가 생긴다"""

colab = """[Colab] 셀마다 따로 실행
  !pip -q install streamlit pdfplumber google-genai
  !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
  !chmod +x cloudflared
  !streamlit run app.py --server.port 8501 &>/dev/null &
  !./cloudflared tunnel --url http://localhost:8501
→ 출력에 나오는 https://....trycloudflare.com 주소를 연다"""

for how in (local, cloud, colab):
    print(how, end="\\n\\n")''',
    tip="처음 띄우면 왼쪽에서 '연습 자료로 해 보기' 를 켠다. 영업 270, 투자 −500, 재무 380, 현금의 증가 150 이 나오고 검산 넷이 통과하면 설치가 제대로 된 것이다. 그다음 저장소의 data/sg_2014.xlsx 와 sg_2014.pdf 를 올려 같은 숫자가 나오는지 본다. Colab 방법은 환경이 자주 바뀌어 막힐 수 있다. 막히면 ① 이나 ② 로 한다.",
    talk=[dict(who="robo", state="thinking", text="삐빅, 연습 자료로 270, −500, 380 이 나오면 설치 성공.")],
)

def stages(ns, out):
    return [
        S("① 내 PC", "명령 두 줄이면 브라우저에 화면이 열린다.", TX(ns["local"], "code", "local")),
        S("② 클라우드", "깃허브 저장소를 연결하면 누구나 열 수 있는 주소가 생긴다.", TX(ns["cloud"], "code", "cloud")),
        S("③ Colab", "터널 프로그램으로 임시 주소를 만든다. 세션이 끝나면 사라진다.", TX(ns["colab"], "code", "colab")),
    ]
