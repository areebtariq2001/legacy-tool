main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checksecrets2_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("required_key")
    out.write("=== required_key context ===\n")
    out.write(content[max(0,idx-300):idx+100] + chr(10) + chr(10))

    idx2 = content.find("webhook_secret")
    out.write("=== webhook_secret context ===\n")
    out.write(content[max(0,idx2-300):idx2+100])
print("CHECKSECRETS2-DONE")