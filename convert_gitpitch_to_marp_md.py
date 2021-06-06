from pathlib import Path

yaml_tmpl = """---
marp: true
header: "{title}"
paginate: true
backgroundColor: #eee
---

"""

# PITCHME.mdを読み込む
pitchme_list = list(Path("./").glob("**/PITCHME.md"))

# ひとつづつ処理
for p in pitchme_list:

    replaced_lines = []
    title = ""
    with p.open(encoding="utf-8") as f:
        for index, line in enumerate(f):
            # タイトルを取得
            if index <= 3 and "# "in line:
                fix_line = line.replace("#", "")
                fix_line = fix_line.removeprefix(" ").removesuffix("\n")
                title += fix_line
            # +++を---にする
            if "+++\n" == line:
                line = "---\n"
            replaced_lines.append(line)

    # print(title)
    # print(replaced_lines)

    # 先頭にyaml情報を埋め込む
    yaml_header = yaml_tmpl.format(title=title)
    # print(yaml_header)

    # PITCHME.mdを slide.mdにして保存。marpとしても書き出す
    export_path = (p.parent / "slide.md")
    with export_path.open("w", encoding="utf-8") as f:
        f.write(yaml_header)
        f.writelines(replaced_lines)
    