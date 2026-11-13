"""그림 지시문 만들기: python3 src/build/make_docs.py  →  docs/IMG_PROMPTS_all.md"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC, ASST, FLY, ROBO = ('chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie',
 'girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans',
 'anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right',
 'boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left')
SCENE = 'the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky.'
# (키, 파일, 제목, 장소(층), 주제 은유, 박사, 조수, 초파리, 주판봇)
C = [
 ('cover_00', 'index.html', '파이썬과 회계데이터 분석 (목차)', '로비 · 고객 접견실',
  'a tall glass office tower shown as a clean architectural scale model on the reception desk, each floor glowing in a different soft color; beside it a small coffee-shop model (the client, Café Koi) with a tiny koi-fish sign shape (no letters)',
  'center-back, pointing at one glowing floor of the tower model', 'at one side behind the reception desk, holding a blank clipboard', 'leaning in to inspect the small coffee-shop model with a magnifier', 'raising its abacus happily toward the top floor of the model'),
 ('cover_01', '01_accounting_basics.html', '재무회계의 기초개념과 회계정보', '1F 기초 진단팀',
  'a large two-pan balance scale on a meeting table: the left pan holds a toy delivery van and a stack of coins (assets), the right pan holds a bank-loan envelope and a small owner\'s piggy bank (liabilities and equity), perfectly level',
  'center-back, adjusting the scale so it stays level', 'placing one coin on the left pan and watching the pointer', 'pointing at the loan envelope on the right pan', 'hugging a bank passbook, delighted by the big balance'),
 ('cover_02', '02_revenue_inventory.html', '회계요소별 정보의 이해 ① 매출과 재고', '2F 매출·재고 진단팀',
  'a café counter with a card terminal; from it a row of blank receipt slips hangs on a clothesline, the oldest slips fading to gray; behind, warehouse shelves of coffee-bean sacks where some sacks are sold (empty outline) and some remain',
  'center-back, pointing along the clothesline of receipts', 'counting the remaining bean sacks with a blank clipboard', 'holding up the oldest, grayest receipt with a doubtful look', 'proudly holding a tall stack of sales slips'),
 ('cover_03', '03_payables_prepaid.html', '회계요소별 정보의 이해 ② 매입과 비용', '3F 구매·비용 진단팀',
  'a big wall calendar with blank squares; a supplier invoice pinned on an early day with a small discount tag, and a six-segment advertising voucher where the segments are being torn off one month at a time into an expense tray',
  'center-back, tapping an early day on the calendar', 'tearing off one segment of the voucher and dropping it into the tray', 'holding the small discount tag up to the light', 'holding its coins close, reluctant to pay early'),
 ('cover_04', '04_fixed_assets_tax.html', '회계요소별 정보의 이해 ③ 자산과 세금', '4F 자산·세무팀',
  'a shiny industrial bakery oven; in front of it, five equal blocks cut from the oven\'s price lined up as steps (straight-line), and beside them five shrinking blocks (declining balance); a small slice of a profit pie being set aside on a plate for tax',
  'center-back, comparing the two rows of blocks', 'placing the next equal block on the row', 'pointing at the shrinking row', 'trying to push all five blocks into the first slot at once'),
 ('cover_05', '05_python_basics.html', '파이썬 기초 — 네 가지 그릇', '5F 데이터 분석실',
  'four containers on a lab bench: a row of numbered lockers in a line (list), a cabinet with name-tag drawers (dict), a tray where every cup is being filled at once by one wide pour (array), and a large glowing spreadsheet grid floating above (DataFrame) that turns into a simple bar chart at its edge',
  'center-back, gesturing from the four containers to the glowing grid', 'opening the first locker in the row', 'peeking into a name-tag drawer with a magnifier', 'pressing one big button and watching the whole tray fill at once'),
 ('cover_06m', '06m_midterm_review.html', '중간 요약정리 및 퀴즈 — 1~5주차', '6M 중간 점검 라운지',
  'a lounge with potted trees and a board holding five blank cards and small quiz buttons, with a green ribbon marking halfway up a miniature tower model',
  'tapping the board', 'handing out blank cards', 'raising a hand to answer', 'holding a big score tally board (no numbers)'),
 ('cover_08', '08_balance_sheet_review.html', '재무상태표 다시 보기 — 재고 평가와 유형자산', '8F 재무상태표 리뷰팀',
  'a supermarket-style milk shelf seen from the side, cartons in three shades (oldest in front, newest at back), with one hand-off lane taking from the front and another taking from the back; next to it a delivery van on a lift with one new tire and one new engine block on a cart',
  'center-back, pointing at the front and back of the shelf', 'taking a carton from the front row', 'taking a carton from the back row and comparing the two', 'polishing the new engine block proudly'),
 ('cover_09', '09_turnover_review.html', '재무제표 Review — 회전율과 시점 차이', '9F 회전율 분석팀',
  'a large glass turnstile-like wheel in the middle of the office: coins enter as boxes of goods, turn into receipt slips, and come out as coins again; a stopwatch-shaped gauge (no digits) shows how fast the wheel turns',
  'center-back, watching the gauge', 'timing one full turn with a blank stopwatch', 'holding one slow box that is stuck in the wheel', 'cranking the wheel faster with both arms'),
 ('cover_10', '10_cashflow_ratios.html', '현금흐름표와 재무분석', '10F 현금흐름·재무비율 진단실',
  'a glass tank of clear blue water (cash) fed and drained by three pipes with colored valves — green (operations), amber (investing), blue (financing) — and on the wall a medical-checkup style panel of eight blank gauges',
  'center-back, reading the eight gauges', 'opening the green valve and watching the water level', 'checking where the amber pipe drains to', 'cheering at a big trophy-shaped profit balloon that is not connected to the tank'),
 ('cover_11', '11_managerial_accounting.html', '관리회계 — 숫자의 한계에서 의사결정까지', '11F 관리회계팀',
  'a large seesaw-like lever on the meeting-room floor: on one end a heavy block (fixed cost) with a small robot arm machine on top, on the other end a stack of sales boxes; a glowing break-even mark on the floor where two light beams (a green revenue beam and a red cost beam) cross',
  'center-back, pointing at the spot where the two beams cross', 'sorting cost blocks into two trays, one tray that moves on wheels and one tray bolted to the floor', 'measuring the lever with a ruler, doubtful about the heavy block', 'hugging the small robot arm machine, eager to install it'),
]
def prompt(k, scene_extra, metaphor, d, a, f, r):
    return f'''Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: {SCENE} This room is {scene_extra}.
All four characters together:
  {DOC}, {d};
  {ASST}, {a};
  {FLY}, {f};
  {ROBO}, {r}.
Visual metaphor of the topic: {metaphor}.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.'''
ROOMS = {'cover_00': 'the ground-floor lobby with a reception desk and an elevator door in the background', 'cover_01': 'a first-floor intake office with a round meeting table', 'cover_02': 'a second-floor review room opening onto a small stock room', 'cover_03': 'a third-floor purchasing office with a wall calendar', 'cover_04': 'a fourth-floor asset room with a demo kitchen corner', 'cover_05': 'a fifth-floor data lab with long benches and monitors', 'cover_06m': 'a glass-walled sky lounge between floors with potted trees', 'cover_08': 'an eighth-floor review room with display shelves and a small garage bay', 'cover_09': 'a ninth-floor analytics room with a central glass machine', 'cover_10': 'a tenth-floor diagnosis room with a water tank and a wall of gauges', 'cover_11': 'an eleventh-floor boardroom with a long table and a factory scale model by the window'}
o = ['''# 그림 지시문 — 파이썬과 회계데이터 분석 (AI 회계 컨설팅 연구실)

흰 배경 페이지용. 모든 그림은 **글자·숫자·로고 없음**, 캐릭터 외형은 `adminmrobo/fruitfly-lab-expressions`의 기본 그림(박사·조수·초파리 연구원·주판봇)을 참고 이미지로 함께 올립니다(인턴은 `images/_sheets/lab6_lineup.png`, 실루엣은 `images/x1`~`x3`). 배경은 연구실이 아니라 **밝은 AI 회계 컨설팅회사(P&A 파트너스) 사무실**입니다.

| 묶음 | 키 | 장수 | 비율 · 크기 | 넣을 자리 |
|---|---|---|---|---|
| ① 시리즈 대표 표지 | series_key | 1 | 21:9 2400×1030 | README 맨 위 → 잘라서 `assets/og_series.jpg`(1200×630) |
| ② 개별 표지 | cover_00 ~ cover_05, cover_06m, cover_08 ~ cover_11 | 11 | 16:9 1920 이상 → 1600×900 WebP | 각 페이지 맨 위(`src/build/covers/cover_XX.webp`), 목차 썸네일·공유 미리보기는 표지에서 자름 |

필수는 **모두 12장**입니다(12층 실습 강의안의 대표 그림은 `pandas-cashflow-lab/docs/`에서 따로 다룹니다). 받는 순서: ① series_key → ② cover_00 → (그림체 확정) → cover_01 ~ cover_11. 요청은 한 대화에 3~5장씩, 같은 비율끼리 묶어 주세요. cover_00을 먼저 받아 그림체를 확인한 뒤 나머지 요청에 참고 그림으로 함께 올립니다.

받은 뒤: 표지를 1600×900 WebP(220 KB 이하)로 줄여 `src/build/covers/cover_00.webp` … `cover_11.webp`, `cover_06m.webp`로 저장하고 `python3 src/build/build.py out`을 다시 돌리면 대체 표지(캐릭터 네 명이 나란히 선 그림)가 자동으로 바뀝니다. 공유 미리보기는 같은 표지를 1200×630 JPG로 잘라 `assets/og/cover_00.jpg` …에 둡니다.

고칠 때(공통): `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text, bright daytime office.`

저장 이름 체크리스트: `series_key.png` · `cover_00.png` · `cover_01.png` · `cover_02.png` · `cover_03.png` · `cover_04.png` · `cover_05.png` · `cover_06m.png` · `cover_08.png` · `cover_09.png` · `cover_10.png` · `cover_11.png`

## ① 시리즈 대표 표지

### series_key — 파이썬과 회계데이터 분석 (대표 그림)

| 항목 | 내용 |
|---|---|
| 키 · 크기 | series_key · 21:9, 2400×1030 이상 |
| 넣을 자리 | README 맨 위, `assets/og_series.jpg` |
| 대체 글(alt) | 연구실 식구 여섯과 방청석의 실루엣 셋이 유리 타워 로비에서 층마다 빛나는 본사 타워 모형과 카페 코이 모형을 둘러싼 장면 |

**Genspark에 붙여 넣기 ↓**
```
시리즈 전체를 대표하는 가로로 긴 표지 그림 1장을 만들어 줘.
- 비율 21:9, 가로 2400px 이상
- 첨부한 참고 이미지의 연구실 식구 여섯(박사·조수·초파리 연구원·주판봇·시아·모아)과 미공개 실루엣 X1·X2·X3를 같은 그림체·같은 외형으로 모두 등장
- 밝은 낮의 AI 회계 컨설팅회사 로비, 아래 가장자리는 흰색으로 자연스럽게 사라지게
- 그림 안에 글자·숫자·로고 없음
아래 영어 프롬프트를 그대로 써 줘.

Series key visual, ultra-wide 21:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: ''' + SCENE + ''' This is the ground-floor lobby.
Center: a tall glass office tower as a clean architectural scale model on a white plinth, about a dozen floors, each floor band glowing in a different soft color (blue, green, red, purple, amber, teal), a few upper floors still gray (not yet opened), a small roof garden with a wireframe globe on top. In front of it a tiny coffee-shop model (the client) with a koi-fish shaped sign (no letters).
Around the tower model, small floating icons rise floor by floor from left to right: a balance scale, a receipt slip, a calendar page, an oven, four containers, a milk shelf, a turning wheel, a water tank with three pipes, a row of gauges, a lever with a heavy block.
All four main characters:
  ''' + DOC + ''', center-back, pointing at one glowing floor;
  ''' + ASST + ''', beside the plinth, holding a blank clipboard;
  ''' + FLY + ''', inspecting the coffee-shop model with a magnifier;
  ''' + ROBO + ''', raising the abacus toward the top floor.
Referees at the right edge: two maid-uniform interns, one with black hair holding a small start flag, one with beige hair holding a blank score board.
Audience at the far left on a lobby bench: three small cute black silhouette creatures (one with a pink ribbon, one with teal glasses glint, one with a yellow bell), seen as silhouettes only.
Composition: all faces inside the central band, bottom edge fades to near-white, the tower model is the most saturated spot.
Mood: a welcoming first day at a friendly consulting firm.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## ② 개별 표지 11장
''']
for k, f, title, place, met, d, a, fl, r in C:
    o.append(f'''
### {k} — {title}

| 항목 | 내용 |
|---|---|
| 키 · 판 | {k} · L (16:9, 1920 이상) |
| 페이지 | `{f}` |
| 장소 | P&A 파트너스 본사 타워 {place} |
| 주제 은유 | {met} |
| 대체 글(alt) | {title}의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 {place}에서 주제 소품을 둘러싼 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 배경은 실험실이 아니라 밝은 회계 컨설팅회사 사무실(유리 타워 안)
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게(흰 벽), 아래 가장자리는 흰 페이지로 자연스럽게 이어지게
- 밤 장면·어두운 배경 금지, 전체적으로 밝은 낮 장면
아래 영어 프롬프트를 그대로 써 줘.

{prompt(k, ROOMS[k], met, d, a, fl, r)}
```
''')
o.append('''
## 참고 — 지금 화면에 쓰이는 그림

- 페이지 맨 위의 3D 본사 타워는 그림 파일이 아니라 three.js로 그립니다(그림 필요 없음).
- 표지 그림을 넣기 전에는 캐릭터 네 명이 나란히 선 대체 표지가 나옵니다.
- 본문의 캐릭터 얼굴은 캐릭터 팩(fruitfly-lab-expressions, 96px)을 그대로 씁니다(새 그림 필요 없음).
- 칸 그림·대결 그림은 이 시리즈에서는 쓰지 않습니다(실험 패널이 그 자리를 대신합니다). 나중에 넣고 싶으면 주차별로 요청해 주세요.
''')
os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)
open(os.path.join(ROOT, 'docs', 'IMG_PROMPTS_all.md'), 'w', encoding='utf-8').write(''.join(o))
print('docs/IMG_PROMPTS_all.md', len(''.join(o)) // 1024, 'KB')
