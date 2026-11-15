"""Run every card's code, capture output + figures, assemble data, write site/index.html.

usage: python3 build/build.py [card_id ...]    (no args = all cards)
"""
import contextlib, glob, importlib.util, io, json, os, sys, tempfile, traceback
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = ROOT   # 결과: repo 맨 위 index.html, assets/img
IMG = os.path.join(SITE, "assets", "img")
sys.path.insert(0, os.path.join(ROOT, "build"))
from snippets import lint

SAMPLE_ID = "20261005"                     # 페이지에 실행 결과를 싣는 표본 학번
SESSION = tempfile.mkdtemp()               # Colab 세션처럼 파일이 남는 폴더 (chain 카드와 한 셀 카드가 함께 쓴다)
CHAIN = {"__name__": "__main__"}           # Colab 노트북처럼 변수가 이어지는 이름공간 (chain=True 카드)

def make_sample():
    """generator.html 의 생성 코드를 node 로 돌려 표본 학번의 CSV 를 만든다 (학생이 받는 파일과 같다)."""
    import subprocess, types, shutil
    subprocess.run(["node", os.path.join(ROOT, "build", "gen_sample.js"), SAMPLE_ID], check=True, capture_output=True)
    src = os.path.join(ROOT, "build", "sample", "재무제표_" + SAMPLE_ID + ".csv")
    def upload():                          # google.colab.files.upload 흉내: 파일을 지금 폴더에 놓고 {이름: 내용} 을 돌려준다
        name = os.path.basename(src)
        shutil.copy(src, name)
        print(f"Saving {name} to {name}")
        return {name: open(name, "rb").read()}
    def download(name):                    # Colab 에서는 브라우저가 파일을 받는다. 출력은 없다
        assert os.path.exists(name), name
    files = types.SimpleNamespace(upload=upload, download=download)
    colab = types.ModuleType("google.colab"); colab.files = files
    google = sys.modules.get("google") or types.ModuleType("google")
    google.colab = colab
    sys.modules["google"] = google; sys.modules["google.colab"] = colab

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def run_card(m):
    c = dict(m.CARD)
    cid = c["id"]
    if c.get("chain") and cid not in ("upload", "split"):   # 이어 실행하는 셀: 앞 셀(5-1·5-2)을 건너뛰면 NameError 대신 안내문
        c["code"] = ('# ▶ 이어서 실행하는 셀: 5장 첫 카드(CSV 올리기)부터 이 카드 앞까지를 같은 노트북에서 차례로 먼저 실행한다\n'
                     'assert "fs" in globals() and "p" in globals(), "앞 셀을 먼저 실행하세요: 5-1 CSV 올리기 → 5-2 두 표로 나누기 → … → 이 셀"\n\n' + c["code"])
    elif cid == "split":
        c["code"] = ('# ▶ 이어서 실행하는 셀: 바로 앞 카드(5-1 CSV 올리기)를 같은 노트북에서 먼저 실행한다\n'
                     'assert "fs" in globals(), "앞 셀을 먼저 실행하세요: 5-1 CSV 올리기 → 이 셀"\n\n' + c["code"])
    lint(c["code"], cid)                      # 들여쓰기·def·for 금지
    assert c.get("xl"), cid + ": 엑셀 설명(xl)이 없다"
    c["xl"] = [list(r) for r in c["xl"]]
    for f in glob.glob(os.path.join(IMG, cid + ".png")) + glob.glob(os.path.join(IMG, cid + "-*.png")):
        os.remove(f)
    imgs = []
    def show(*a, **k):
        for num in plt.get_fignums():
            fig = plt.figure(num)
            name = cid + ("" if not imgs else f"-{len(imgs)}") + ".png"
            fig.savefig(os.path.join(IMG, name), dpi=80, bbox_inches="tight", facecolor="white")
            imgs.append("assets/img/" + name)
        plt.close("all")
    plt.close("all")
    orig_show = plt.show; plt.show = show
    chain = c.get("chain", False)
    ns = CHAIN if chain else {"__name__": "__main__"}
    buf = io.StringIO()
    cwd = os.getcwd(); tmp = SESSION if (chain or c.get("session")) else tempfile.mkdtemp()
    try:
        os.chdir(tmp)
        plt.rcParams.update(matplotlib.rcParamsDefault)
        with contextlib.redirect_stdout(buf):
            exec(compile(c["code"], cid, "exec"), ns)
        if plt.get_fignums(): show()
    finally:
        os.chdir(cwd); plt.show = orig_show
    out = buf.getvalue().rstrip("\n")
    c["output"] = out
    c["imgs"] = imgs
    c["stages"] = m.stages(ns, out)
    c.setdefault("tip", ""); c.setdefault("talk", [])
    c.pop("kit", None); c.pop("session", None)
    return c

def main(only):
    make_sample()
    files = sorted(glob.glob(os.path.join(ROOT, "build", "cards", "*.py")))
    cards, bad = [], []
    for p in files:
        m = load(p)
        if only and m.CARD["id"] not in only:
            continue
        try:
            cards.append(run_card(m)); print("ok  ", m.CARD["id"], len(cards[-1]["imgs"]), "img")
        except Exception:
            bad.append(m.CARD["id"]); print("FAIL", m.CARD["id"]); traceback.print_exc()
    if only:
        os.makedirs(os.path.join(ROOT, "build", "_preview"), exist_ok=True)
        for c in cards:
            json.dump(c, open(os.path.join(ROOT, "build", "_preview", c["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
        return bad
    ids = [c["id"] for c in cards]
    assert len(ids) == len(set(ids)), "duplicate ids"
    tpl = open(os.path.join(ROOT, "build", "template.html"), encoding="utf-8").read()
    data = json.dumps(cards, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("__CARD_DATA__", data).replace("__CARD_COUNT__", str(len(cards)))
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(html)
    print(len(cards), "cards ->", os.path.join(SITE, "index.html"), "fail:", bad)
    return bad

if __name__ == "__main__":
    sys.exit(1 if main(set(sys.argv[1:])) else 0)
