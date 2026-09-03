import subprocess
result = subprocess.run(["git", "ls-files", "-z"], capture_output=True)
raw_files = result.stdout.split(b"\x00")
target = None
for f in raw_files:
    if b"kh" in f and b"backend" in f and not f.endswith(b".py") and not f.endswith(b".txt") and not f.endswith(b".json") and not f.endswith(b".md"):
        target = f
        break

with open("weird_file_result2.txt", "wb") as out:
    if target:
        out.write(b"Genuinely-found-target-bytes: " + target + b"\n")
        r2 = subprocess.run(["git", "rm", "-f", "--"], input=target, capture_output=True)
        out.write(b"removal-returncode: " + str(r2.returncode).encode() + b"\n")
        out.write(b"stdout: " + r2.stdout + b"\n")
        out.write(b"stderr: " + r2.stderr + b"\n")
    else:
        out.write(b"NOT-FOUND")
print("WEIRD-FILE-REMOVE2-COMPLETED")