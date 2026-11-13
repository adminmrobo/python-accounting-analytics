# 그림 지시문 — 파이썬과 회계데이터 분석 (AI 회계 컨설팅 연구실)

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
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This is the ground-floor lobby.
Center: a tall glass office tower as a clean architectural scale model on a white plinth, about a dozen floors, each floor band glowing in a different soft color (blue, green, red, purple, amber, teal), a few upper floors still gray (not yet opened), a small roof garden with a wireframe globe on top. In front of it a tiny coffee-shop model (the client) with a koi-fish shaped sign (no letters).
Around the tower model, small floating icons rise floor by floor from left to right: a balance scale, a receipt slip, a calendar page, an oven, four containers, a milk shelf, a turning wheel, a water tank with three pipes, a row of gauges, a lever with a heavy block.
All four main characters:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, pointing at one glowing floor;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, beside the plinth, holding a blank clipboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, inspecting the coffee-shop model with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, raising the abacus toward the top floor.
Referees at the right edge: two maid-uniform interns, one with black hair holding a small start flag, one with beige hair holding a blank score board.
Audience at the far left on a lobby bench: three small cute black silhouette creatures (one with a pink ribbon, one with teal glasses glint, one with a yellow bell), seen as silhouettes only.
Composition: all faces inside the central band, bottom edge fades to near-white, the tower model is the most saturated spot.
Mood: a welcoming first day at a friendly consulting firm.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## ② 개별 표지 11장

### cover_00 — 파이썬과 회계데이터 분석 (목차)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_00 · L (16:9, 1920 이상) |
| 페이지 | `index.html` |
| 장소 | P&A 파트너스 본사 타워 로비 · 고객 접견실 |
| 주제 은유 | a tall glass office tower shown as a clean architectural scale model on the reception desk, each floor glowing in a different soft color; beside it a small coffee-shop model (the client, Café Koi) with a tiny koi-fish sign shape (no letters) |
| 대체 글(alt) | 파이썬과 회계데이터 분석 (목차)의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 로비 · 고객 접견실에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is the ground-floor lobby with a reception desk and an elevator door in the background.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, pointing at one glowing floor of the tower model;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side behind the reception desk, holding a blank clipboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, leaning in to inspect the small coffee-shop model with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, raising its abacus happily toward the top floor of the model.
Visual metaphor of the topic: a tall glass office tower shown as a clean architectural scale model on the reception desk, each floor glowing in a different soft color; beside it a small coffee-shop model (the client, Café Koi) with a tiny koi-fish sign shape (no letters).
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_01 — 재무회계의 기초개념과 회계정보

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 1920 이상) |
| 페이지 | `01_accounting_basics.html` |
| 장소 | P&A 파트너스 본사 타워 1F 기초 진단팀 |
| 주제 은유 | a large two-pan balance scale on a meeting table: the left pan holds a toy delivery van and a stack of coins (assets), the right pan holds a bank-loan envelope and a small owner's piggy bank (liabilities and equity), perfectly level |
| 대체 글(alt) | 재무회계의 기초개념과 회계정보의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 1F 기초 진단팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a first-floor intake office with a round meeting table.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, adjusting the scale so it stays level;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, placing one coin on the left pan and watching the pointer;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the loan envelope on the right pan;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, hugging a bank passbook, delighted by the big balance.
Visual metaphor of the topic: a large two-pan balance scale on a meeting table: the left pan holds a toy delivery van and a stack of coins (assets), the right pan holds a bank-loan envelope and a small owner's piggy bank (liabilities and equity), perfectly level.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_02 — 회계요소별 정보의 이해 ① 매출과 재고

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9, 1920 이상) |
| 페이지 | `02_revenue_inventory.html` |
| 장소 | P&A 파트너스 본사 타워 2F 매출·재고 진단팀 |
| 주제 은유 | a café counter with a card terminal; from it a row of blank receipt slips hangs on a clothesline, the oldest slips fading to gray; behind, warehouse shelves of coffee-bean sacks where some sacks are sold (empty outline) and some remain |
| 대체 글(alt) | 회계요소별 정보의 이해 ① 매출과 재고의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 2F 매출·재고 진단팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a second-floor review room opening onto a small stock room.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, pointing along the clothesline of receipts;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, counting the remaining bean sacks with a blank clipboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding up the oldest, grayest receipt with a doubtful look;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, proudly holding a tall stack of sales slips.
Visual metaphor of the topic: a café counter with a card terminal; from it a row of blank receipt slips hangs on a clothesline, the oldest slips fading to gray; behind, warehouse shelves of coffee-bean sacks where some sacks are sold (empty outline) and some remain.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_03 — 회계요소별 정보의 이해 ② 매입과 비용

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9, 1920 이상) |
| 페이지 | `03_payables_prepaid.html` |
| 장소 | P&A 파트너스 본사 타워 3F 구매·비용 진단팀 |
| 주제 은유 | a big wall calendar with blank squares; a supplier invoice pinned on an early day with a small discount tag, and a six-segment advertising voucher where the segments are being torn off one month at a time into an expense tray |
| 대체 글(alt) | 회계요소별 정보의 이해 ② 매입과 비용의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 3F 구매·비용 진단팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a third-floor purchasing office with a wall calendar.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, tapping an early day on the calendar;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, tearing off one segment of the voucher and dropping it into the tray;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding the small discount tag up to the light;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, holding its coins close, reluctant to pay early.
Visual metaphor of the topic: a big wall calendar with blank squares; a supplier invoice pinned on an early day with a small discount tag, and a six-segment advertising voucher where the segments are being torn off one month at a time into an expense tray.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_04 — 회계요소별 정보의 이해 ③ 자산과 세금

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9, 1920 이상) |
| 페이지 | `04_fixed_assets_tax.html` |
| 장소 | P&A 파트너스 본사 타워 4F 자산·세무팀 |
| 주제 은유 | a shiny industrial bakery oven; in front of it, five equal blocks cut from the oven's price lined up as steps (straight-line), and beside them five shrinking blocks (declining balance); a small slice of a profit pie being set aside on a plate for tax |
| 대체 글(alt) | 회계요소별 정보의 이해 ③ 자산과 세금의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 4F 자산·세무팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a fourth-floor asset room with a demo kitchen corner.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, comparing the two rows of blocks;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, placing the next equal block on the row;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the shrinking row;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, trying to push all five blocks into the first slot at once.
Visual metaphor of the topic: a shiny industrial bakery oven; in front of it, five equal blocks cut from the oven's price lined up as steps (straight-line), and beside them five shrinking blocks (declining balance); a small slice of a profit pie being set aside on a plate for tax.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_05 — 파이썬 기초 — 네 가지 그릇

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9, 1920 이상) |
| 페이지 | `05_python_basics.html` |
| 장소 | P&A 파트너스 본사 타워 5F 데이터 분석실 |
| 주제 은유 | four containers on a lab bench: a row of numbered lockers in a line (list), a cabinet with name-tag drawers (dict), a tray where every cup is being filled at once by one wide pour (array), and a large glowing spreadsheet grid floating above (DataFrame) that turns into a simple bar chart at its edge |
| 대체 글(alt) | 파이썬 기초 — 네 가지 그릇의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 5F 데이터 분석실에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a fifth-floor data lab with long benches and monitors.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, gesturing from the four containers to the glowing grid;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, opening the first locker in the row;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, peeking into a name-tag drawer with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, pressing one big button and watching the whole tray fill at once.
Visual metaphor of the topic: four containers on a lab bench: a row of numbered lockers in a line (list), a cabinet with name-tag drawers (dict), a tray where every cup is being filled at once by one wide pour (array), and a large glowing spreadsheet grid floating above (DataFrame) that turns into a simple bar chart at its edge.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_06m — 중간 요약정리 및 퀴즈 — 1~5주차

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06m · L (16:9, 1920 이상) |
| 페이지 | `06m_midterm_review.html` |
| 장소 | P&A 파트너스 본사 타워 6M 중간 점검 라운지 |
| 주제 은유 | a lounge with potted trees and a board holding five blank cards and small quiz buttons, with a green ribbon marking halfway up a miniature tower model |
| 대체 글(alt) | 중간 요약정리 및 퀴즈 — 1~5주차의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 6M 중간 점검 라운지에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a glass-walled sky lounge between floors with potted trees.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, tapping the board;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, handing out blank cards;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, raising a hand to answer;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, holding a big score tally board (no numbers).
Visual metaphor of the topic: a lounge with potted trees and a board holding five blank cards and small quiz buttons, with a green ribbon marking halfway up a miniature tower model.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_08 — 재무상태표 다시 보기 — 재고 평가와 유형자산

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_08 · L (16:9, 1920 이상) |
| 페이지 | `08_balance_sheet_review.html` |
| 장소 | P&A 파트너스 본사 타워 8F 재무상태표 리뷰팀 |
| 주제 은유 | a supermarket-style milk shelf seen from the side, cartons in three shades (oldest in front, newest at back), with one hand-off lane taking from the front and another taking from the back; next to it a delivery van on a lift with one new tire and one new engine block on a cart |
| 대체 글(alt) | 재무상태표 다시 보기 — 재고 평가와 유형자산의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 8F 재무상태표 리뷰팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is an eighth-floor review room with display shelves and a small garage bay.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, pointing at the front and back of the shelf;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, taking a carton from the front row;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, taking a carton from the back row and comparing the two;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, polishing the new engine block proudly.
Visual metaphor of the topic: a supermarket-style milk shelf seen from the side, cartons in three shades (oldest in front, newest at back), with one hand-off lane taking from the front and another taking from the back; next to it a delivery van on a lift with one new tire and one new engine block on a cart.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_09 — 재무제표 Review — 회전율과 시점 차이

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_09 · L (16:9, 1920 이상) |
| 페이지 | `09_turnover_review.html` |
| 장소 | P&A 파트너스 본사 타워 9F 회전율 분석팀 |
| 주제 은유 | a large glass turnstile-like wheel in the middle of the office: coins enter as boxes of goods, turn into receipt slips, and come out as coins again; a stopwatch-shaped gauge (no digits) shows how fast the wheel turns |
| 대체 글(alt) | 재무제표 Review — 회전율과 시점 차이의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 9F 회전율 분석팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a ninth-floor analytics room with a central glass machine.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, watching the gauge;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, timing one full turn with a blank stopwatch;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding one slow box that is stuck in the wheel;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, cranking the wheel faster with both arms.
Visual metaphor of the topic: a large glass turnstile-like wheel in the middle of the office: coins enter as boxes of goods, turn into receipt slips, and come out as coins again; a stopwatch-shaped gauge (no digits) shows how fast the wheel turns.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_10 — 현금흐름표와 재무분석

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_10 · L (16:9, 1920 이상) |
| 페이지 | `10_cashflow_ratios.html` |
| 장소 | P&A 파트너스 본사 타워 10F 현금흐름·재무비율 진단실 |
| 주제 은유 | a glass tank of clear blue water (cash) fed and drained by three pipes with colored valves — green (operations), amber (investing), blue (financing) — and on the wall a medical-checkup style panel of eight blank gauges |
| 대체 글(alt) | 현금흐름표와 재무분석의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 10F 현금흐름·재무비율 진단실에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is a tenth-floor diagnosis room with a water tank and a wall of gauges.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, reading the eight gauges;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, opening the green valve and watching the water level;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, checking where the amber pipe drains to;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, cheering at a big trophy-shaped profit balloon that is not connected to the tank.
Visual metaphor of the topic: a glass tank of clear blue water (cash) fed and drained by three pipes with colored valves — green (operations), amber (investing), blue (financing) — and on the wall a medical-checkup style panel of eight blank gauges.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### cover_11 — 관리회계 — 숫자의 한계에서 의사결정까지

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_11 · L (16:9, 1920 이상) |
| 페이지 | `11_managerial_accounting.html` |
| 장소 | P&A 파트너스 본사 타워 11F 관리회계팀 |
| 주제 은유 | a large seesaw-like lever on the meeting-room floor: on one end a heavy block (fixed cost) with a small robot arm machine on top, on the other end a stack of sales boxes; a glowing break-even mark on the floor where two light beams (a green revenue beam and a red cost beam) cross |
| 대체 글(alt) | 관리회계 — 숫자의 한계에서 의사결정까지의 표지: 박사, 조수, 초파리 연구원, 주판봇이 AI 회계 컨설팅회사 11F 관리회계팀에서 주제 소품을 둘러싼 장면 |

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

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: the bright, airy office of an AI accounting consulting firm in a glass tower, soft daylight through floor-to-ceiling windows, clean white walls and pale gray-blue furniture (#ffffff to #f6f7fb), gentle shadows, pale blue monitor glow, small accents of magenta (#a8329f), green (#138a52) and blue (#2563c9). High-key image that blends into a white web page; no dark background, no night sky. This room is an eleventh-floor boardroom with a long table and a factory scale model by the window.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center-back, pointing at the spot where the two beams cross;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sorting cost blocks into two trays, one tray that moves on wheels and one tray bolted to the floor;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, measuring the lever with a ruler, doubtful about the heavy block;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, hugging the small robot arm machine, eager to install it.
Visual metaphor of the topic: a large seesaw-like lever on the meeting-room floor: on one end a heavy block (fixed cost) with a small robot arm machine on top, on the other end a stack of sales boxes; a glowing break-even mark on the floor where two light beams (a green revenue beam and a red cost beam) cross.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner light and simple (plain white wall); let the bottom edge fade to near-white so the image melts into a white page; the topic prop is the most saturated spot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 참고 — 지금 화면에 쓰이는 그림

- 페이지 맨 위의 3D 본사 타워는 그림 파일이 아니라 three.js로 그립니다(그림 필요 없음).
- 표지 그림을 넣기 전에는 캐릭터 네 명이 나란히 선 대체 표지가 나옵니다.
- 본문의 캐릭터 얼굴은 캐릭터 팩(fruitfly-lab-expressions, 96px)을 그대로 씁니다(새 그림 필요 없음).
- 칸 그림·대결 그림은 이 시리즈에서는 쓰지 않습니다(실험 패널이 그 자리를 대신합니다). 나중에 넣고 싶으면 주차별로 요청해 주세요.
