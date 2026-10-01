main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkstre_result.txt", "w", encoding="utf-8") as out:
    out.write("=== login_user exception handler ===\n")
    idx = content.find('f"Login failed: {e}"')
    out.write(content[max(0,idx-100):idx+50] + chr(10) + chr(10))

    out.write("=== register_user exception handler ===\n")
    idx2 = content.find("def register_user")
    idx2_end = content.find("\ndef ", idx2+20)
    body2 = content[idx2:idx2_end]
    ridx = body2.find("except Exception as e")
    out.write(body2[max(0,ridx-50):ridx+150] if ridx != -1 else "no-except-found")
print("CHECKSTRE-DONE")