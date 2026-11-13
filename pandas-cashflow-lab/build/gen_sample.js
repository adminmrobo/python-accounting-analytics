// generator.html 의 생성 코드를 그대로 돌려 학번별 CSV 를 만든다.  usage: node build/gen_sample.js 20261234 [더 많은 학번...]
const fs = require("fs"), path = require("path");
const html = fs.readFileSync(path.join(__dirname, "..", "generator.html"), "utf8");
const src = html.split('<script id="gen">')[1].split("</script>")[0];
const g = new Function(src + "; return {generate, toCSV};")();
const out = process.argv[2] === "--check" ? null : path.join(__dirname, "sample");
if (out) fs.mkdirSync(out, { recursive: true });
let bad = 0;
const ids = process.argv[2] === "--check" ? Array.from({ length: 3000 }, (_, i) => String(20260000 + i * 7)) : process.argv.slice(2);
for (const id of ids) {
  const x = g.generate(id);
  const v = (r) => [r[4] === "" ? 0 : r[4], r[5]];
  const sum = (k, j) => x.rows.filter((r) => r[1] === k).reduce((a, r) => a + v(r)[j], 0);
  const ok0 = sum("자산", 0) === sum("부채", 0) + sum("자본", 0), ok1 = sum("자산", 1) === sum("부채", 1) + sum("자본", 1);
  const cashOk = x.check.cash[1] - x.check.cash[0] === x.check.cfo + x.check.cfi + x.check.cff;
  const pos = x.rows.every((r) => r[3] === "감가상각누계액" || (r[4] === "" || r[4] >= 0) && r[5] >= 0);
  if (!(ok0 && ok1 && cashOk && pos)) { bad++; if (bad < 5) console.log("BAD", id, ok0, ok1, cashOk, pos, x.rows.filter(r=>r[5]<0)); }
  if (out) fs.writeFileSync(path.join(out, "재무제표_" + id + ".csv"), "﻿" + g.toCSV(x));
}
console.log(ids.length, "개 학번, 맞지 않는 것:", bad);
