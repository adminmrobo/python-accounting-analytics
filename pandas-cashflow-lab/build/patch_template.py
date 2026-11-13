"""원본 틀(보면서 배우는 pandas 의 index.html 에서 자료를 뺀 것)을 이 책의 template.html 로 바꾼다. 한 번만 실행."""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
def rep(a, b):
    global h
    assert a in h, a[:60]
    h = h.replace(a, b)
T = "pandas 로 만드는 현금흐름표"
h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{T} — 손익계산서와 재무상태표로 간접법 현금흐름표를 pandas 로 만든다. 학번으로 만든 회사의 CSV 를 Colab 에 올려 현금흐름표·차트·재무비율을 만들고, 생성AI 로 분석보고서를 완성한다. 과제 안내 포함.">', h, count=1)
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
rep('<p class="sub">카페·편의점·쇼핑몰 장부로 보는 명령어 72장</p>', '<p class="sub">손익계산서·재무상태표에서 간접법으로, 학번별 회사 분석보고서까지 __CARD_COUNT__장</p>')
rep("<p>명령어마다 표가 한 단계씩 움직이는 그림으로 본다. 코드는 Colab 새 셀에 그대로 붙여 넣으면 파일 없이 실행된다.</p>",
    '<p>카드마다 표가 한 단계씩 움직이는 그림으로 본다. 코드는 Colab 새 셀에 그대로 붙여 넣으면 파일 없이 실행된다.</p><p style="margin-top:6px"><a href="generator.html">재무제표 생성기</a> · <a href="colab/pandas_cashflow_lab.ipynb">실습 노트북</a> · <a href="#flow">실습 순서</a> · <a href="#homework">과제 안내</a></p>')
rep('aria-label="명령어 고르기"', 'aria-label="카드 고르기"')
rep('placeholder="명령어나 뜻으로 찾기 (예: merge, 합계)"', 'placeholder="명령어나 뜻으로 찾기 (예: merge, 검산)"')
rep("이 책의 식구 넷 — 장부 상담소에서 함께 표를 읽는다", "이 책의 식구 넷 — 연구실에서 함께 현금흐름표를 만든다")
rep("늘 한 번 더 의심한다. 빠진 줄, 숨은 공백을 찾는다.", "늘 한 번 더 의심한다. 뒤집힌 부호, 두 번 센 줄을 찾는다.")
rep("<q>그 숫자, 처음 보는 데이터로도 맞아?</q>", "<q>세 활동 더한 게 현금 증감이랑 맞아?</q>")
rep("예제 속 가게와 숫자는 모두 지어낸 것이다. 주판봇은", "0~4장은 (주)SG화학 2014년 강의용 숫자, 5장부터는 학번으로 만든 가상 회사다. 교육용 자료이며 세무·회계·투자 자문이 아니다. 주판봇은")
rep('var SEEN_KEY="lpv-seen";', 'var SEEN_KEY="pcf-seen";')
rep('if(h!=="ch-list") window.scrollTo(0,0); else { var t=$("ch-list"); if(t) t.scrollIntoView(); } return;',
    'var t=h?$(h):null; if(t && h!=="cover") t.scrollIntoView(); else window.scrollTo(0,0); return;')

# ── 엑셀로 따라 하기 표 ──
rep(".tip{margin:16px 0 0;", """.xlbox{margin-top:18px}
.xlwrap{overflow-x:auto}
table.xlt{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.55;background:#fff;color:#1C2620}
.xlt th,.xlt td{border-top:1px solid #DDE3DE;padding:8px 14px;text-align:left;vertical-align:top}
.xlt th{background:#F1F7F2;font-weight:600;font-size:.82rem;color:#17633A;border-top:0}
.xlt td:first-child{font-family:var(--mono);font-size:.84rem;width:42%;word-break:break-all;background:#FAFBF9}
.xlbox .ph{background:#DDEFE2;border-bottom-color:#BFDCC8}
.av-sia{background:#34363F}.av-moa{background:#B89C74}.av-x{background:#1B1A2E;color:#E9709A}
.tip{margin:16px 0 0;""")
rep('    <p class="tip" id="tip" hidden></p>', """    <section class="panel xlbox" aria-label="엑셀로 따라 하기">
      <div class="ph"><span>엑셀로 따라 하기 <small>코드 한 줄 = 엑셀 한 동작</small></span></div>
      <div class="xlwrap"><table class="xlt"><thead><tr><th>파이썬 코드</th><th>엑셀로 하면</th></tr></thead><tbody id="xl"></tbody></table></div>
    </section>
    <p class="tip" id="tip" hidden></p>""")
rep('  var tip=$("tip");', """  var xb=$("xl"); xb.innerHTML=""; (c.xl||[]).forEach(function(r){ var tr=el("tr"), a=el("td"), b=el("td"); a.textContent=r[0]; b.textContent=r[1]; tr.appendChild(a); tr.appendChild(b); xb.appendChild(tr); });
  var tip=$("tip");""")
rep('robo:{name:"주판봇",b:"주",face:"robo_idle"}};', 'robo:{name:"주판봇",b:"주",face:"robo_idle"},sia:{name:"시아",b:"시",face:"sia_neutral"},moa:{name:"모아",b:"모",face:"moa_neutral"},x:{name:"방청석 X1 · X2 · X3",b:"X",face:"x_crowd"}};')
rep('<summary>이 책의 식구 넷 — 연구실에서 함께 현금흐름표를 만든다</summary>', '<summary>이 책의 식구들 — 연구실에서 함께 현금흐름표를 만든다</summary>')
rep("""      <p class="note">주판봇은 연구실 캐릭터이며""", """      <div class="grid">
        <div class="mate"><span class="av av-sia" data-k="sia_neutral">시</span><div><b>시아 · 인턴</b><small>검산이 통과했는지 판정한다. 말수가 적고 숫자만 본다.</small><q>판정. 통과입니다.</q></div></div>
        <div class="mate"><span class="av av-moa" data-k="moa_neutral">모</span><div><b>모아 · 인턴</b><small>고친 곳과 다른 줄을 빠짐없이 적어 둔다.</small><q>기록해 뒀어요.</q></div></div>
        <div class="mate"><span class="av av-x" data-k="x_crowd">X</span><div><b>X1 · X2 · X3 · 미공개 식구</b><small>방청석에서 지켜본다. 아직 정체를 밝히지 않았다.</small><q>…</q></div></div>
      </div>
      <p class="note">주판봇은 연구실 캐릭터이며""")
h = h.replace("보면서 배우는 pandas", T)
rep('"내 파일로 할 때: "', '"참고: "')
rep("#cover section{padding:42px 0 6px}", "#cover section{padding:42px 0 6px;scroll-margin-top:56px}")
rep("<b>박사 · 상담소장</b>", "<b>박사 · 연구실장</b>")
rep(".brand p{margin:0;font-size:.82rem;color:var(--ink-2);line-height:1.5}", ".brand p{margin:0;font-size:.82rem;color:var(--ink-2);line-height:1.5}\n.brand p a{color:inherit}")
left = [m.group() for m in re.finditer("72장|보면서 배우는|편의점|카페|(?<![0-9])장부|상담소", h)]
assert not left, left
open(dst, "w", encoding="utf-8").write(h)
print("ok", len(h))
