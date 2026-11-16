# -*- coding: utf-8 -*-
"""P&E 글로벌 본사 타워 — 3D 첫 화면(건물 안내)

목차(index)는 건물 전체를, 주차 쪽은 그 주차가 들어 있는 층을 3D로 보여 주고
층 평면(방 = 이 쪽의 칸)과 둘러보는 순서를 안내한다.

- build.py / build_extra.py 가 nav 바로 뒤, 표지 그림 앞에 tower_html(key)를 넣는다.
- 이미 빌드된 HTML에는 add_tower.py 로 같은 블록을 넣거나 갈아 끼운다(표식 <!--tower:start--> … <!--tower:end-->).
- three.js 는 CDN(jsdelivr)에서 불러온다. 불러오지 못하면 오른쪽 안내판만으로 쓸 수 있다.
"""
import os, json, html

B = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(B, 'tower.css'), encoding='utf-8').read()
JS = open(os.path.join(B, 'tower.js'), encoding='utf-8').read()
THREE_VER = '0.170.0'

COMPANY = dict(ko='P&A 파트너스', en='Python & Accounting Partners', hq='본사 타워',
               motto='재무제표를 읽고(Accounting) 파이썬으로 계산하는(Python) AI 회계 컨설팅회사',
               note='가상의 AI 회계 컨설팅회사입니다. 층마다 한 팀이 있고, 팀마다 그 주차의 회계 도구로 고객사 「카페 코이」를 진단합니다.')

CLOCKS = [('서울 본사', 'Asia/Seoul'), ('싱가포르', 'Asia/Singapore'), ('런던', 'Europe/London'), ('뉴욕', 'America/New_York')]

PAL = ['#3f5fa8', '#138a52', '#d23f2c', '#2563c9', '#a8329f', '#b77800', '#14899a', '#7a45d6']

def LES(a, b, c, sa, sb, sc):
    return [('three', '안내 데스크', '3줄 요약'), ('cast', '팀 라운지', '연구실 식구'), ('lv1', a, '칸 ① ' + sa), ('lv2', b, '칸 ② ' + sb), ('lv3', c, '칸 ③ ' + sc),
            ('dash', '상황실', '한눈에 보는 대시보드'), ('duel', '대결 홀', '초파리 대 주판봇 대결'), ('sum', '정리 데스크', '정리'), ('kg', '자료실', '지식 색인 · 꾸러미')]

REV = [('three', '안내 데스크', '3줄 요약'), ('cast', '팀 라운지', '연구실 식구'), ('summary', '요약 갤러리', '1부 요약'), ('orig', '문제세트 시험장', '2부 문제세트'),
       ('calc', '업무 계산실', '3부 업무 계산'), ('score', '점수판', '주차별 점수'), ('kg', '자료실', '지식 색인 · 꾸러미')]

IDX = [('three', '안내 데스크', '3줄 요약'), ('map', '층별 안내판', '주차 지도'), ('keys', '한 줄 핵심 게시판', '한 줄 핵심 모음'), ('dash', '종합 상황실', '종합 대시보드'),
       ('path', '개념 계단', '개념 사다리'), ('how', '식구 라운지', '식구 · 사용법'), ('about', '자료 보관실', '자료와 원칙')]

SOON = [('map', '입주 준비 중', '목차의 주차 지도')]
def F(key, label, file, dept, en, branch, title, ep, biz, rooms, soon=False):
    return dict(key=key, label=label, file=file, dept=dept, en=en, branch=branch, title=title, ep=ep, biz=biz, rooms=rooms, soon=soon)

# 아래에서 위로: 로비 → 1~5층 → 6M 라운지 → 7~12층 → 옥상
FLOORS = [
 F('00', 'L', 'index.html', '로비 · 고객 접견실', 'Lobby & Client Desk', '서울 본사', '목차 — 파이썬과 회계데이터 분석', '목차',
   '본사 타워의 로비입니다. 고객사 「카페 코이」의 의뢰서를 받고, 층별 안내판에서 팀(주차)을 골라 올라갑니다.', IDX),
 F('01', '1F', '01_accounting_basics.html', '기초 진단팀', 'Accounting Foundations', '고객사 카페 코이 · 설립 3개월', '재무회계의 기초개념과 회계정보', '01주차',
   '새 고객사의 거래를 처음 받아 적는 팀이에요. 거래 한 줄이 회계등식을 어떻게 움직이는지, 이익과 통장 잔고가 왜 다른지, 거래 묶음이 어떻게 재무제표 세 장이 되는지 봅니다.',
   LES('회계등식실', '발생주의 회의실', '재무제표 조립실', '회계등식', '발생주의', '시산표와 재무제표')),
 F('02', '2F', '02_revenue_inventory.html', '매출·재고 진단팀', 'Revenue & Inventory', '고객사 카페 코이 · 2분기', '회계요소별 정보의 이해 ① 매출·재고', '02주차',
   '팔았는데 아직 못 받은 돈(매출채권)과 사 놓고 아직 못 판 물건(재고자산)을 추적하는 팀이에요. 매출 숫자 뒤의 회수와 원가를 함께 봅니다.',
   LES('채권 회수실', '대손 심사실', '원가·재고 창고', '매출과 매출채권', '대손충당금', '매출원가와 재고')),
 F('03', '3F', '03_payables_prepaid.html', '구매·비용 진단팀', 'Payables & Expenses', '고객사 카페 코이 · 3분기', '회계요소별 정보의 이해 ② 매입·비용', '03주차',
   '돈이 나가는 두 통로를 보는 팀이에요. 외상으로 산 물건값(매입채무)을 언제 갚을지, 미리 낸 돈(선급비용)을 어느 달 비용으로 풀지, 고정비와 변동비를 가릅니다.',
   LES('매입채무 결제실', '선급비용 배분실', '손익분기 분석실', '매입채무와 결제조건', '선급비용', '고정비와 변동비')),
 F('04', '4F', '04_fixed_assets_tax.html', '자산·세무팀', 'Fixed Assets & Tax', '고객사 카페 코이 · 연말 결산', '회계요소별 정보의 이해 ③ 자산·세금', '04주차',
   '오븐·차량처럼 오래 쓰는 자산의 값을 여러 해에 나눠 비용으로 보내고(감가상각), 이익에서 법인세를 떼어 당기순이익까지 내려가는 팀이에요.',
   LES('자산 등록실', '감가상각 계산실', '세무 조정실', '자산화와 정액법', '정률법', '법인세와 순이익')),
 F('05', '5F', '05_python_basics.html', '데이터 분석실', 'Python Data Lab', '전 층 공용 · 브라우저 실습실', '파이썬 기초 — 카페 코이로 배우는 네 가지 그릇', '05주차',
   '아래 네 층이 쓰는 계산을 코드로 바꿔 주는 팀이에요. 값을 줄 세우고(list), 이름표를 붙이고(dict), 통째로 계산하고(array), 표로 묶어(DataFrame) 그림으로 확인합니다.',
   LES('목록·이름표 보관실', '표 계산실', '집계·시각화 스튜디오', 'list와 dict', 'array와 DataFrame', '묶어 세기와 그림')),
 F('06m', '6M', '06m_midterm_review.html', '중간 점검 라운지', 'Midterm Lounge', '1~5주차 요약 · 문제세트', '중간 요약정리 및 퀴즈 — 1~5주차', '중간 점검',
   '1~5층에서 배운 것을 요약하고, 주차별 문제세트와 업무 장면 계산 문제로 점검하는 라운지예요.', REV),
 F('07', '7F', 'index.html#map', '현금흐름 심화팀', 'Cash Flow Advanced', '입주 준비 중', '현금흐름표 심화 — 정체·성장·침체 기업', '준비 중',
   '강의 교안이 준비되는 대로 입주할 층입니다. 지금은 10층 현금흐름·재무비율 진단실에서 현금흐름표를 먼저 볼 수 있어요.', SOON, True),
 F('08', '8F', '08_balance_sheet_review.html', '재무상태표 리뷰팀', 'Balance Sheet Review', '고객사 여러 곳 · 리뷰', '재무상태표 다시 보기 — 재고 평가와 유형자산', '08주차',
   '재무상태표의 항목을 위에서 아래로 다시 읽는 팀이에요. 같은 재고도 평가 방법에 따라 이익이 달라지고, 수리와 개량은 가는 곳이 다르다는 것을 숫자로 확인합니다.',
   LES('재고 평가실', '지출 분류실', '상각 비교실', '재고자산 평가', '자본적 지출과 수익적 지출', '정액법과 정률법 비교')),
 F('09', '9F', '09_turnover_review.html', '회전율 분석팀', 'Turnover Analytics', '고객사 여러 곳 · 리뷰', '재무제표 Review — 회전율과 시점 차이', '09주차',
   '손익계산서의 흐름과 재무상태표의 잔액을 한 숫자(회전율)로 묶는 팀이에요. 채권이 몇 주 만에 걷히는지, 재고가 몇 주 묶이는지, 비용과 현금이 얼마나 어긋나는지 봅니다.',
   LES('채권 회전실', '재고 회전실', '시점 차이 조정실', '매출채권 회전율', '재고자산 회전율', '미지급·선급·법인세')),
 F('10', '10F', '10_cashflow_ratios.html', '현금흐름·재무비율 진단실', 'Cash Flow & Ratios', '고객사 여러 곳 · 종합 진단', '현금흐름표와 재무분석', '10주차',
   '현금이 어디서 들어와 어디로 나갔는지 세 활동으로 나누고, 여덟 가지 비율로 회사를 진단하는 팀이에요.',
   LES('직접법 계산실', '간접법 조정실', '비율 진단실', '현금흐름표와 직접법', '간접법', '재무비율 여덟 가지')),
 F('11', '11F', '11_managerial_accounting.html', '관리회계팀', 'Managerial Accounting', '고객사 제조업체 · 자동화 투자 검토', '관리회계 — 숫자의 한계에서 의사결정까지', '11주차',
   '밖에 보고된 숫자가 어디까지 믿을 만한지 확인하고, 같은 숫자를 회사 안의 결정에 쓰기 좋게 다시 나누는 팀이에요. 손익분기점과 영업레버리지로 자동화 설비 32.5억 원을 판단합니다.',
   LES('숫자 점검실', '손익분기 분석실', '투자 심사실', '숫자의 한계', '공헌이익과 손익분기점', '영업레버리지와 자동화 투자')),
 F('12', '12F', 'pandas-cashflow-lab/', '현금흐름표 자동화 실습실', 'pandas Cash Flow Lab', '전 층 공용 · Colab 실습', 'pandas 로 만드는 현금흐름표', '실습',
   '맨 위층 실습실입니다. 학번으로 만든 회사의 재무제표 CSV를 Colab에 올려, 손익계산서와 재무상태표에서 간접법 현금흐름표·차트·재무비율을 pandas로 직접 만들어요. 이 층은 따로 만든 실습 강의안으로 이어집니다.',
   [('top', '실습 강의안', 'pandas 로 만드는 현금흐름표')]),
 F('rf', 'R', 'index.html#about', '옥상 정원', 'Roof Garden', '서울 본사', '자료와 원칙', '옥상',
   '간판과 정원이 있는 옥상입니다. 이 사이트를 만든 자료와 원칙은 목차 맨 아래에 있어요.', SOON, True),
]
for _f in FLOORS:
    if _f['key'] == '12': _f['extra'] = [('pandas-cashflow-lab/generator.html', '학번 재무제표 생성기 바로 가기'), ('pandas-cashflow-lab/colab/pandas_cashflow_lab.ipynb', 'Colab 노트북 받기')]
for i, f in enumerate(FLOORS):
    f['color'] = '#5d6278' if f['key'] in ('00',) else ('#138a52' if f['key'] in ('06m',) else ('#9aa3b5' if f['soon'] else PAL[(i - 1) % len(PAL)]))
KEYS = [f['key'] for f in FLOORS]
BYKEY = {f['key']: f for f in FLOORS}

e = lambda s: html.escape(str(s), quote=True)

def floor_name(f):
    return f'{f["label"]} {f["dept"]}'

def _data(cur):
    fl = [dict(key=f['key'], label=f['label'], dept=f['dept'], en=f['en'], branch=f['branch'], title=f['title'], ep=f['ep'], file=f['file'],
               biz=f['biz'], color=f['color'], soon=f['soon'], extra=f.get('extra', []), rooms=[dict(id=a, name=b, sec=c) for a, b, c in f['rooms']]) for f in FLOORS]
    return dict(cur=cur, company=COMPANY, floors=fl)

def _route_items(f):
    o = []
    for i, (a, b, c) in enumerate(f['rooms']):
        tag = 'EV' if i == 0 else str(i)
        o.append(f'<li data-i="{i}"><a href="#{a}"><i>{tag}</i><b>{e(b)}</b><span>{e(c)}</span></a></li>')
    return ''.join(o)

def _panel_floor(f):
    i = KEYS.index(f['key'])
    live = [g for g in FLOORS if not g['soon']]; j = live.index(f)
    dn = live[j - 1] if j > 1 else None          # 1F의 아래는 로비(목차)
    up = live[j + 1] if j + 1 < len(live) else None
    el = []
    el.append(f'<a class="dn" href="{dn["file"]}" title="{e(dn["title"])}">▼ {e(floor_name(dn))}</a>' if dn else '<span class="dn off">▼ 아래층 없음</span>')
    el.append('<a class="lob" href="index.html">로비 · 목차</a>')
    el.append(f'<a class="up" href="{up["file"]}" title="{e(up["title"])}">▲ {e(floor_name(up))}</a>' if up else '<span class="up off">▲ 위층은 입주 준비 중</span>')
    first = '엘리베이터에서 내리면 안내 데스크(3줄 요약)부터 들러요. 걷는 사람 표시가 둘러보는 순서를 따라 움직입니다.'
    return f'''<aside class="tw-panel" aria-label="{e(f["label"])} 층 안내">
<p class="tw-co"><b>{e(COMPANY["ko"])}</b> {e(COMPANY["hq"])} · <span>{e(COMPANY["en"])}</span></p>
<div class="tw-fl"><span class="tw-badge" style="--c:{f["color"]}">{e(f["label"])}</span><div><h2>{e(f["dept"])}</h2><p class="tw-en">{e(f["en"])} · {e(f["branch"])}</p></div></div>
<p class="tw-ep"><b>{e(f["ep"])}</b> {e(f["title"])}</p>
<p class="tw-biz">{e(f["biz"])}</p>
<h3>이 층 둘러보는 순서</h3>
<p class="tw-tip">{first}</p>
<ol class="tw-route">{_route_items(f)}</ol>
<nav class="tw-elev" aria-label="엘리베이터 — 층 이동">{"".join(el)}</nav>
</aside>'''

def _panel_index(f):
    rows = []
    for g in reversed(FLOORS[1:]):
        rows.append(f'<li data-k="{g["key"]}"><a href="{g["file"]}"><span class="tw-badge" style="--c:{g["color"]}">{e(g["label"])}</span><b>{e(g["dept"])}</b><span>{e(g["ep"])} · {e(g["title"])}</span></a></li>')
    rows.append(f'<li data-k="00" class="here"><a href="#three"><span class="tw-badge" style="--c:{f["color"]}">L</span><b>로비 · 안내 데스크</b><span>지금 계신 곳 · 이 목차 쪽</span></a></li>')
    rows.append('<li data-k="cafe"><a href="cafe-quiz/"><span class="tw-badge" style="--c:#b5651d">☕</span><b>카페 · 퀴즈방</b><span>타워 옆 별관 · 기말고사 모의 퀴즈</span></a></li>')
    clocks = ''.join(f'<span data-tz="{tz}"><b>{c}</b><i>--:--</i></span>' for c, tz in CLOCKS)
    return f'''<aside class="tw-panel" aria-label="층별 안내판">
<p class="tw-co"><b>{e(COMPANY["ko"])}</b> {e(COMPANY["hq"])} · <span>{e(COMPANY["en"])}</span></p>
<h2>층별 안내판</h2>
<p class="tw-biz">{e(COMPANY["motto"])}. 아홉 팀이 한 층씩 쓰고, 5층과 7층 사이 라운지(6M)에서 중간 요약정리와 퀴즈를 봅니다. 맨 위 12층은 현금흐름표 자동화 실습실이고, 회색 7층은 입주 준비 중이에요. 타워 왼쪽 카페는 기말고사 모의 퀴즈를 푸는 퀴즈방이에요. 건물의 층을 누르거나 아래 안내판에서 골라 올라가세요.</p>
<div class="tw-clock" aria-label="본사와 해외 고객사 시각">{clocks}</div>
<ol class="tw-dir">{"".join(rows)}</ol>
<p class="tw-note">{e(COMPANY["note"])}</p>
</aside>'''

def tower_html(key):
    f = BYKEY[key]
    idx = key == '00'
    panel = _panel_index(f) if idx else _panel_floor(f)
    tools = ('<button type="button" data-v="b" class="on">건물 전체</button><button type="button" data-v="spin" aria-pressed="true">자동 회전</button>' if idx else
             '<button type="button" data-v="b">건물 전체</button><button type="button" data-v="p" class="on">이 층 평면</button>')
    hint = '드래그로 돌려 보고 층을 누르면 안내 카드가 열려요' if idx else '방을 누르면 그 칸으로 내려갑니다 · 드래그로 돌려 보기'
    cap = (f'{COMPANY["ko"]} 본사 타워 3D 모형: 로비부터 옥상까지 15개 층, 층마다 한 팀(주차)' if idx else
           f'{COMPANY["ko"]} 본사 타워 3D 모형에서 {f["label"]} {f["dept"]}을(를) 건물 밖으로 꺼내 보여 주는 층 평면')
    data = json.dumps(_data(key), ensure_ascii=False).replace('</', '<\\/')
    imap = json.dumps({'imports': {'three': f'https://cdn.jsdelivr.net/npm/three@{THREE_VER}/build/three.module.js',
                                   'three/addons/': f'https://cdn.jsdelivr.net/npm/three@{THREE_VER}/examples/jsm/'}})
    return f'''<!--tower:start-->
<style>
{CSS}
</style>
<section class="tower{' tw-idx' if idx else ''}" id="tower" data-floor="{key}" aria-label="{e(COMPANY['ko'])} 본사 타워 — 건물 안내">
<div class="tw-stage" role="img" aria-label="{e(cap)}">
<div class="tw-cv" aria-hidden="true"></div><div class="tw-labels" aria-hidden="true"></div>
<div class="tw-tools">{tools}</div>
<p class="tw-hint">{hint}</p>
<div class="tw-card" hidden></div>
<div class="tw-err" hidden>3D 건물을 불러오지 못했습니다(인터넷 연결 · WebGL 확인). 오른쪽 안내판으로 그대로 이동할 수 있어요.</div>
<div class="tw-load">건물을 짓는 중…</div>
</div>
{panel}
</section>
<script type="application/json" id="towerData">{data}</script>
<script type="importmap">{imap}</script>
<script type="module">
{JS}
</script>
<!--tower:end-->
'''

NAV_LINK = '<a href="#tower">건물 안내</a>'
