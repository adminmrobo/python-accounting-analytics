"""docs/ASSIGNMENT.md (표지의 과제 안내와 같은 내용)를 만든다.  usage: python build/make_docs.py"""
import html, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))

c = open(os.path.join(ROOT, "build", "cover.html"), encoding="utf-8").read()
s = c[c.index('<section id="homework"'):c.index('<section aria-labelledby="ckit-h"')]
s = re.sub(r'<h2[^>]*>.*?</h2>', '# 과제 안내: 내 회사의 현금흐름표와 분석보고서\n', s, flags=re.S)
s = re.sub(r'<h3>■ (.*?)</h3>', r'\n## \1\n', s)
s = re.sub(r'<tr><th>(.*?)</th><th>(.*?)</th><th>(.*?)</th></tr>', r'| \1 | \2 | \3 |\n|---|---|---|', s)
s = re.sub(r'<tr><th>(.*?)</th><th>(.*?)</th></tr>', r'| \1 | \2 |\n|---|---|', s)
s = re.sub(r'<tr><td colspan="2">(.*?)</td><td class="n">(.*?)</td></tr>', r'| \1 | | \2 |', s)
s = re.sub(r'<tr>(.*?)</tr>', lambda m: "| " + " | ".join(re.findall(r'<td[^>]*>(.*?)</td>', m.group(1))) + " |", s)
s = re.sub(r'<li>(.*?)</li>', r'- \1', s)
s = re.sub(r'<a href="#([^"]+)">(.*?)</a>', r'\2(#\1)', s)
s = re.sub(r'</?b>', '**', s); s = re.sub(r'</?code>', '`', s)
s = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', s)
s = html.unescape(re.sub(r'<[^>]+>', '', s))
s = re.sub(r'\n{3,}', '\n\n', "\n".join(l.strip() for l in s.splitlines())).strip()
open(os.path.join(ROOT, "docs", "ASSIGNMENT.md"), "w", encoding="utf-8").write(
    s + "\n\n---\n괄호 안의 #이름 은 책의 카드 주소다 (예: `.../#hw_compare`). 배점은 기본안이며 수업 공지가 우선한다.\n")

print("docs/ASSIGNMENT.md")
