from lib import *

CARD = dict(
    id="save_png", ch="9. 저장하고 내려받기", cmd='fig.savefig("…png", dpi=150)', chain=True,
    title="차트 네 장을 한 그림으로 모아 저장한다", excel="차트를 그림으로 저장",
    desc="plt.subplots(2, 2) 는 그림 한 장에 칸 네 개를 만든다. axes[0, 0] 은 왼쪽 위 칸이다. 7·8장의 차트를 한 칸씩 다시 그려 한 장으로 모으고 savefig 로 PNG 파일을 만든다. "
         "보고서에 붙이거나 생성AI 에 함께 올릴 수 있다. 칸마다 그리는 줄은 7·8장과 같고, ax 자리만 axes[행, 열] 로 바뀌었다.",
    code='''fig, axes = plt.subplots(2, 2, figsize=(11, 7))
axes[0, 0].bar(x, lower, color="#4472C4")
axes[0, 0].bar(x, middle, bottom=lower, color="#A9BEE3")
axes[0, 0].bar(x, upper, bottom=np.add(lower, middle), color="#2E9E5B")
axes[0, 0].set(title="Balance sheet structure")
axes[0, 1].bar(b_labels, b_height, bottom=b_bottom, color=b_colors)
axes[0, 1].axhline(0, color="black", linewidth=0.8)
axes[0, 1].set(title="Cash bridge")
op_labels = ["NI", "Dep", "Gain", "AR", "Inv", "Pre", "AP", "Wage", "CFO"]
op_height = np.concatenate([[steps[0]], steps[1:], [run[-1]]])
op_bottom = np.concatenate([[0, steps[0]], run[1:-1], [0]])
op_colors = ["#1F3A5F"] + list(np.where(steps[1:] >= 0, "#2E9E5B", "#C9382A")) + ["#1F3A5F"]
axes[1, 0].bar(op_labels, op_height, bottom=op_bottom, color=op_colors)
axes[1, 0].axhline(0, color="black", linewidth=0.8)
axes[1, 0].set(title="Net income to operating cash")
axes[1, 1].barh(pct["eng"], pct["값"], color=np.where(pct["판정"] == "양호", "#2E9E5B", "#C9382A"))
axes[1, 1].scatter(pct["기준"], pct["eng"], color="black", marker="|", s=200)
axes[1, 1].invert_yaxis()
axes[1, 1].set(title="Ratios in % vs reference")
fig.suptitle(f"Student {sid} (KRW mn)")
fig.tight_layout()
png_name = f"차트_{sid}.png"
fig.savefig(png_name, dpi=150)
files.download(png_name)
plt.show()
print("저장:", png_name)''',
    xl=[
        ("plt.subplots(2, 2)", "시트 하나에 차트 네 개를 2 × 2 로 배치한다."),
        ("axes[0, 0].bar(...) … axes[1, 1].barh(...)", "7장 bs_chart · cash_bridge · ni_to_cfo, 8장 ratio_signal 의 차트를 각 칸에 하나씩 놓는다."),
        ("fig.suptitle(...)", "차트 위 빈 셀에 제목을 적는다."),
        ("fig.savefig(png_name, dpi=150)", "차트를 오른쪽 클릭 → 그림으로 저장 (네 개를 함께 선택해 그룹으로 묶고 저장)."),
    ],
    tip="7장의 x · lower · middle · upper, cash_bridge 카드의 b_labels · b_height · b_bottom · b_colors, ni_to_cfo 카드의 steps · run, 8장의 pct 를 그대로 쓴다. 이 셀만 따로 실행하면 이름이 없다는 오류가 난다. 앞 카드를 먼저 실행한다.",
)

def stages(ns, out):
    return [
        S("칸 네 개", "axes[행, 열] 로 칸을 고른다.",
          TX("axes[0, 0] 재무상태표 구조   axes[0, 1] 현금 다리\naxes[1, 0] 순이익 → 영업현금   axes[1, 1] 재무비율", "code", "배치")),
        S("한 장", f"{ns['png_name']} 로 저장했다.", IMG("save_png")),
    ]
