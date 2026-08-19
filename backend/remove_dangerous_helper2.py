with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "def _run_single_sandbox(code, timeout_s=8):"
start_idx = content.find(start_marker)
print("start_idx:", start_idx)
if start_idx != -1:
    end_idx = content.find("\ndef ", start_idx + 10)
    print("end_idx:", end_idx)
    if end_idx != -1:
        removed_chunk = content[start_idx:end_idx]
        content = content[:start_idx] + content[end_idx+1:]
        with open("main.py", "w", encoding="utf-8") as f:
            f.write(content)
        print("DANGEROUS-HELPER-REMOVED-SUCCESSFULLY")
        print("Removed chars:", len(removed_chunk))
    else:
        print("FAILED - could not find end boundary")
else:
    print("FAILED - could not find function")