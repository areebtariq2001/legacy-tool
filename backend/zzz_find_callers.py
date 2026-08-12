with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("zzz_callers_out.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "_run_single_sandbox(" in line and "def _run_single_sandbox" not in line:
            out.write(str(i+1) + ": " + line)

print("DONE")