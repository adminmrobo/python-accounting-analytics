"""원본 틀(보면서 배우는 pandas 의 index.html 에서 자료를 뺀 것)을 이 책의 template.html 로 바꾼다. 한 번만 실행."""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
def rep(a, b):
    global h
    assert a in h, a[:60]
    h = h.replace(a, b)
T = "pandas 로 만드는 현금흐름표"
h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{T} — 손익계산서와 재무상태표로 간접법 현금흐름표를 코드로 만들고, 엑셀·PDF 를 생성AI 로 읽어 자동으로 바꾸는 앱까지 만든다. 표가 단계별로 움직이는 그림과 Colab 코드, 과제 안내 포함.">', h, count=1)
rep("@media (max-width:820px){#cover .missions", """#cover .steps{counter-reset:st;list-style:none;margin:0;padding:0;display:grid;gap:14px}
#cover .steps li{counter-increment:st;display:grid;grid-template-columns:54px minmax(0,1fr);gap:14px;align-items:start;background:var(--panel);border:3px solid var(--line);box-shadow:4px 4px 0 #0d0a1c;padding:12px 16px}
#cover .steps li::before{content:counter(st);font-family:var(--px);font-size:22px;color:#13141f;background:var(--amber);width:44px;height:44px;display:grid;place-items:center;border:3px solid #13141f}
#cover .steps h4{font-family:var(--px);margin:0 0 4px;font-size:17px;color:var(--cyan)}
#cover .steps p{margin:0;font-size:15px;color:#d8d0f3;word-break:keep-all}
#cover .steps code,#cover .hw code{font-family:"Nanum Gothic Coding",monospace;background:#13141f;border:1px solid var(--line);padding:0 5px;font-size:.92em;color:var(--green)}
#cover .hw{padding:18px 22px;margin-bottom:18px}
#cover .hw h3{font-family:var(--px);margin:0 0 8px;color:var(--amber);font-size:18px}
#cover .hw ul,#cover .hw ol{margin:0;padding-left:22px}#cover .hw li{margin:3px 0;word-break:keep-all}
#cover .hw table{border-collapse:collapse;width:100%;font-size:15px}
#cover .hw th,#cover .hw td{border:2px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
#cover .hw th{font-family:var(--px);font-size:13.5px;color:var(--muted);font-weight:400}
#cover .hw td.n{text-align:right;font-family:var(--px);color:var(--amber);white-space:nowrap}
#cover .hw .note{color:var(--muted);font-size:14px;margin:10px 0 0}
#cover .tscroll{overflow-x:auto}
@media (max-width:820px){#cover .missions""")
a = h.index('<div id="cover">'); b = h.index('<div class="mob">')
h = h[:a] + open(src.rsplit("/", 1)[0] + "/cover.html" if "/" in src else "cover.html", encoding="utf-8").read() + h[b:]
rep('<p class="sub">카페·편의점·쇼핑몰 장부로 보는 명령어 72장</p>', '<p class="sub">손익계산서·재무상태표에서 간접법으로, 생성AI 앱까지 __CARD_COUNT__장</p>')
rep("<p>명령어마다 표가 한 단계씩 움직이는 그림으로 본다. 코드는 Colab 새 셀에 그대로 붙여 넣으면 파일 없이 실행된다.</p>",
    '<p>카드마다 표가 한 단계씩 움직이는 그림으로 본다. 코드는 Colab 새 셀에 그대로 붙여 넣으면 파일 없이 실행된다.</p><p style="margin-top:6px"><a href="#app-guide">앱 만드는 순서</a> · <a href="#homework">과제 안내</a></p>')
rep('aria-label="명령어 고르기"', 'aria-label="카드 고르기"')
rep('placeholder="명령어나 뜻으로 찾기 (예: merge, 합계)"', 'placeholder="명령어나 뜻으로 찾기 (예: merge, 검산)"')
rep("이 책의 식구 넷 — 장부 상담소에서 함께 표를 읽는다", "이 책의 식구 넷 — 장부 상담소에서 함께 현금흐름표를 만든다")
rep("늘 한 번 더 의심한다. 빠진 줄, 숨은 공백을 찾는다.", "늘 한 번 더 의심한다. 뒤집힌 부호, 두 번 센 줄을 찾는다.")
rep("<q>그 숫자, 처음 보는 데이터로도 맞아?</q>", "<q>세 활동 더한 게 현금 증감이랑 맞아?</q>")
rep("예제 속 가게와 숫자는 모두 지어낸 것이다. 주판봇은", "예제는 (주)SG화학 2014년 강의용 숫자다. 교육용 자료이며 세무·회계·투자 자문이 아니다. 주판봇은")
rep('var SEEN_KEY="lpv-seen";', 'var SEEN_KEY="pcf-seen";')
rep('if(h!=="ch-list") window.scrollTo(0,0); else { var t=$("ch-list"); if(t) t.scrollIntoView(); } return;',
    'var t=h?$(h):null; if(t && h!=="cover") t.scrollIntoView(); else window.scrollTo(0,0); return;')
h = h.replace("보면서 배우는 pandas", T)
left = [m.group() for m in re.finditer("72장|보면서 배우는|편의점|카페", h)]
assert not left, left
open(dst, "w", encoding="utf-8").write(h)
print("ok", len(h))
