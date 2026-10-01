main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifywebhook_result.txt", "w", encoding="utf-8") as out:
    idx1 = content.find("def process_github_webhook")
    out.write("=== process_github_webhook FOUND: " + str(idx1 != -1) + " ===\n")
    if idx1 != -1:
        idx1_end = content.find("\ndef ", idx1+20)
        out.write(content[idx1:idx1_end] + chr(10) + chr(10))

    out.write("=== scan_entropy_secrets high_count check ===\n")
    idx2 = content.find("def scan_entropy_secrets")
    idx2_end = content.find("\ndef ", idx2+20)
    out.write(content[idx2:idx2_end])
print("VERIFYWEBHOOK-DONE")