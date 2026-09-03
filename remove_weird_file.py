import subprocess
result = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
weird_files = [f for f in result.stdout.split(chr(10)) if "kh" in f and "backend/" in f and f.endswith((".py",)) == False]
with open("weird_file_result.txt", "w", encoding="utf-8") as out:
    out.write(str(weird_files))
    for wf in weird_files:
        r2 = subprocess.run(["git", "rm", "-f", wf], capture_output=True, text=True)
        out.write(chr(10) + wf + " removal-code: " + str(r2.returncode))
print("WEIRD-FILE-REMOVE-COMPLETED")