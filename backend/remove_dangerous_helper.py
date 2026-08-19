with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _run_single_sandbox(code, timeout_s=8):
    import subprocess as _sp2
    import tempfile as _tf2
    import os as _os2
    try:
        with _tf2.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
            tmp.write(code)
            tmp_path = tmp.name
        try:
            result = _sp2.run(["python3", tmp_path], timeout=timeout_s, capture_output=True, text=True)
            return {"returncode": result.returncode, "stdout": (result.stdout or "")[:1000], "stderr": (result.stderr or "")[:1000], "timed_out": False}
        except _sp2.TimeoutExpired:
            return {"returncode": None, "stdout": "", "stderr": "Execution exceeded time limit", "timed_out": True}
        finally:
            try:
                _os2.remove(tmp_path)
            except Exception:
                pass
    except Exception as e:
        return {"returncode": None, "stdout": "", "stderr": str(e), "timed_out": False}

'''

new = ''''''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("DANGEROUS-HELPER-REMOVED-SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")