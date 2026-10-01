main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifymore_result.txt", "w", encoding="utf-8") as out:
    out.write("=== has_key regex transformation (not migration-rules list) ===\n")
    idx = content.find("has_key(")
    n = 0
    while idx != -1 and n < 5:
        out.write("--- " + str(n+1) + " ---\n")
        out.write(content[max(0,idx-150):idx+100] + chr(10) + chr(10))
        idx = content.find("has_key(", idx+1)
        n += 1

    out.write("=== jailbreak check function ===\n")
    idx2 = content.find("def _check_jailbreak_output")
    idx2_end = content.find("\ndef ", idx2+20)
    out.write(content[idx2:idx2_end] + chr(10) + chr(10))

    out.write("=== GitHub owner/repo regex ===\n")
    idx3 = content.find('r"^[\\w.-]+$"')
    out.write(content[max(0,idx3-100):idx3+200])
print("VERIFYMORE-DONE")