from lib import *

CARD = dict(
    id="save_csv", ch="9. 저장하고 내려받기", cmd='to_csv(encoding="utf-8-sig") · files.download()', chain=True,
    title="현금흐름표와 재무비율을 CSV 로 저장해 내려받는다", excel="다른 이름으로 저장 → CSV UTF-8",
    desc="to_csv 는 표를 CSV 파일로 저장한다. encoding=\"utf-8-sig\" 를 주면 엑셀에서 열어도 한글이 깨지지 않는다. index=False 는 왼쪽의 줄 번호를 빼고 저장한다. "
         "파일 이름에 학번을 넣어 두면 과제 파일이 섞이지 않는다. files.download 는 Colab 폴더의 파일을 내 컴퓨터로 내려받게 한다. "
         "저장한 파일을 다시 읽어 숫자가 그대로인지 확인한다.",
    code='''cf_name = f"현금흐름표_{sid}.csv"
ratio_name = f"재무비율_{sid}.csv"
cf.to_csv(cf_name, index=False, encoding="utf-8-sig")
ratio.to_csv(ratio_name, index=False, encoding="utf-8-sig")
files.download(cf_name)
files.download(ratio_name)

check_cf = pd.read_csv(cf_name)                     # 다시 읽어 확인
print(cf_name, "→", len(check_cf), "줄, 합계", check_cf["금액"].sum(), "(현금 증감", d["현금"], ")")
print(ratio_name, "→", len(pd.read_csv(ratio_name)), "줄")''',
    xl=[
        ('cf.to_csv(cf_name, index=False, encoding="utf-8-sig")', "'현금흐름표' 시트를 선택 → 파일 → 다른 이름으로 저장 → 파일 형식 'CSV UTF-8(쉼표로 분리)' → 이름 현금흐름표_학번.csv"),
        ("ratio.to_csv(...)", "'재무비율' 시트도 같은 방법으로 저장한다. (CSV 는 시트 한 장만 저장된다)"),
        ("files.download(cf_name)", "저장한 파일을 과제 폴더로 옮긴다."),
        ("pd.read_csv(cf_name)", "저장한 CSV 를 다시 열어 숫자를 확인한다."),
    ],
    tip="files.download 가 아무 반응이 없으면 브라우저가 여러 파일 내려받기를 막은 것이다. 주소창 오른쪽의 차단 아이콘에서 허용하거나, Colab 왼쪽 폴더에서 파일 이름 옆 ⋮ → 다운로드를 누른다.",
    talk=[dict(who="moa", text="파일 이름에 학번이 들어가서 안 섞여요. 기록 끝!")],
)

def stages(ns, out):
    return [
        S("두 파일", "현금흐름표와 재무비율을 학번이 든 이름으로 저장한다.",
          TX(f"Colab 폴더\n ├ 재무제표_{ns['sid']}.csv   (올린 파일)\n ├ {ns['cf_name']}\n └ {ns['ratio_name']}", "code", "파일")),
        S("다시 읽기", "저장한 파일의 줄 수와 합계가 그대로다.", TX(out, "out", "출력")),
    ]
