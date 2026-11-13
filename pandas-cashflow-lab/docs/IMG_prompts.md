# 대표 그림 제작 지시문 — 「이익과 현금이 안 맞는다」

지금 `assets/hero/hero.jpg` 는 '보면서 배우는 pandas' 의 그림을 임시로 쓴 것이다. 아래 지시문으로 새 그림을 만들어 같은 이름(1536×1024, jpg)으로 바꿔 넣는다.

- 화풍: 기존 대표 그림과 같은 16비트 픽셀 아트 (fruitfly-lab-expressions 의 정본 화풍)
- 등장: 박사 · 조수(하루) · 초파리 연구원 · 주판봇 · 시아 · 모아 · 미공개 X1 · X2 · X3 (아홉 식구 전원)
- 장면: 손익계산서의 이익과 실제 현금이 맞지 않아 모두 당혹스러워하지만, 박사와 조수를 중심으로 차이를 계단으로 메워 가며 해내는 모습
- 글자 · 숫자 · 로고는 넣지 않는다. 하얀 로봇은 쓰지 않는다 (주판봇은 베이지색 상자형 레트로 컴퓨터 로봇)

## 넣는 법

- 비율 3:2, 가장 큰 해상도 (결과를 1536×1024 로 맞춘다)
- 참고 그림으로 함께 넣기: ① 여섯 식구 단체 `images/_sheets/lab6_lineup.png` ② 시아·모아 설정 시트 `refs/original/sia_sheet.png`, `moa_sheet.png` ③ 미공개 방청객 시트 `X1_crowd`, `X2_crowd`, `X3_crowd` ④ 화풍 기준으로 지금의 `assets/hero/hero.jpg`
- 앞에 붙일 한국어 한 줄: *"참고 그림의 캐릭터 디자인과 픽셀 아트 화풍을 그대로 지켜서, 아래 영어 프롬프트의 장면을 한 장으로 그려 줘. 글자와 숫자는 넣지 마."*

## 프롬프트 A (기본: 당혹과 해결이 한 장에)

```
Detailed 16-bit SNES-era pixel art scene, 3:2 wide composition, cozy research lab at 7pm, warm amber desk lamps and deep navy shadows, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood.

Center back wall: a large green chalkboard. On its left side stands a tall stack of pale paper sheets with a small upward arrow (the profit on paper). On its right side sits a clearly shorter pile of gold coins (the real cash). The two piles obviously do not match in height. Between them, a staircase of five colored blocks (blue, green, red, orange, purple) is half built, bridging from the paper stack toward the coin pile. No text, no numbers anywhere on the board.

Front left, the two who are solving it:
- the Doctor, a chibi scientist with round glasses, black hair with one white streak, white lab coat over a black vest and tie, standing on a small step stool, confidently placing the fourth block onto the staircase with one hand and pointing at the gap with a wooden pointer in the other, focused smile;
- Haru the assistant, a girl researcher with pink hair in two round buns with a navy streak, blue eyes, lavender hoodie under a white lab coat, holding two paper sheets side by side (one in each hand) and looking back and forth between them, eyebrows raised, a sweat drop on her cheek, mouth slightly open in puzzlement, yet handing the next block up to the Doctor with her elbow.

Front right, the checkers:
- the Fruit Fly Researcher, an anthropomorphic fruit fly with a black body, big red compound eyes, a blue helmet with a gold stripe and pink-blue cables, white lab coat and transparent wings, crouching and inspecting one block of the staircase through a magnifying glass, one eye narrowed in doubt;
- JUPANBOT, a boxy beige retro CRT-monitor robot with rounded corners and thick dark brown outlines, a dark green screen face drawn with mint-green pixel blocks, a short antenna topped with one tiny red-brown abacus bead, gray segmented arms with mitten hands, two small dark gray tank treads, holding a small wooden abacus; its screen shows a flustered face with a wavy pixel mouth and two sweat drops, small gear icons floating beside its head as it recalculates.

Middle right, at a small judges' desk:
- Sia, a calm maid intern with long straight jet-black hair to the waist, side-swept bangs, gray eyes, silver drop earrings, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a soft gray bow, long white frilled apron; she holds up a small blank round judging paddle, head tilted, one eyebrow raised, not yet deciding;
- Moa, a gentle maid intern with long wavy ash-beige hair, white frilled maid headband with a thin white ribbon, big amber-brown eyes, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron; she is writing quickly on a blank clipboard, eyes wide with surprise, a small sweat drop.

Back right, on a low bench, three mysterious unrevealed characters drawn as cute solid silhouettes, each filled with one flat very dark navy-black color with a thin purple rim light, two round plain white dot eyes, two small pink blush pixels, friendly and not scary, all three tilting their heads in confusion with tiny white squiggle marks above them:
- X1: chibi girl silhouette with a long side ponytail tied with a big bright pink bow (the bow is the only colored part);
- X2: chibi silhouette with a round beret and round glasses showing two small teal reflections;
- X3: very small chibi silhouette in a hood with cat ears and an oversized lab coat, two yellow pompoms on the hood strings, standing on the bench to see better.

On the desk in the foreground: an open laptop showing a simple upload-arrow icon and a small grid, a few scattered coins, two more colored blocks waiting to be placed.

Everyone looks puzzled that the paper stack and the coin pile do not match, but the staircase is clearly getting finished: the mood is "confused, yet solving it together". No text, no letters, no numbers, no logos, no watermark.
```

## 프롬프트 B (대안: 해낸 직후)

A 와 같은 방, 같은 식구, 같은 화풍. 달라지는 부분만 적는다.

```
Same lab, same nine characters, same pixel art style as before. The staircase of five colored blocks on the chalkboard is now complete and connects the paper stack to the coin pile perfectly. The Doctor lowers the pointer with a proud smile, Haru raises both paper sheets above her head in relief with sparkles around her, the Fruit Fly Researcher gives a small approving nod with arms crossed, JUPANBOT's screen shows a content pixel face with a green check mark beside its head, Sia raises her blank round paddle firmly as a verdict, Moa claps with the clipboard tucked under her arm, and the three silhouettes X1, X2, X3 cheer with tiny white sparkle marks. A few faces still show a leftover sweat drop from the earlier confusion. No text, no letters, no numbers, no logos.
```

## 네거티브

```
text, letters, numbers, words, signage, question mark symbol, watermark, logo, realistic photo, 3D render, smooth vector art, anti-aliased painting, blurry,
extra fingers, distorted face, off-model, different character design, missing character, duplicated character,
white round robot, white robot head, yellow or golden robot eyes, floating robot,
scary silhouette, horror, villain, sharp teeth, glowing red eyes on silhouettes, full color clothing on silhouettes,
maid headdress on the black-haired intern, glasses on the interns,
banknotes with numbers, stock charts with numbers, real bank logos, weapons, alcohol, cigarettes
```

## 확인할 것

- 아홉 식구가 모두 있고 서로 겹쳐 가려지지 않는다 (X3 는 작으니 벤치 위에 세운다)
- 종이 더미와 동전 더미의 높이가 한눈에 다르다. 그 사이를 다섯 색 계단이 잇는다 (간접법 다섯 계단)
- 당혹한 표정(땀방울, 갸웃, 치켜든 눈썹)과 해내는 동작(블록 놓기, 돋보기, 주판, 기록)이 함께 보인다
- 칠판 · 서류 · 클립보드 · 판정 패들 · 노트북 화면에 글자와 숫자가 없다
- 주판봇은 베이지색 상자형이고 화면 얼굴이 민트색 픽셀이다

## 그림을 넣은 뒤

`build/cover.html` 의 대표 그림 alt 문장을 아래로 바꾸고 `build/patch_template.py` → `build/build.py` 를 다시 돌린다.

> 밤의 연구실. 칠판 왼쪽의 높은 서류 더미와 오른쪽의 낮은 동전 더미 사이에 다섯 색 계단이 놓이고 있다. 박사가 발판에 올라 블록을 끼우고, 조수는 서류 두 장을 번갈아 보며 블록을 건넨다. 초파리 연구원은 돋보기로 계단을 살피고, 주판봇은 당황한 얼굴로 주판을 튕긴다. 시아는 판정 패들을 든 채 고개를 갸웃하고, 모아는 놀란 눈으로 기록한다. 뒤쪽 벤치에서 미공개 식구 셋이 고개를 기울이고 있다.
