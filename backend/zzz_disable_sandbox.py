with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def run_sandboxed_migration_test(migrated_code, filename):
    if not filename.lower().endswith(".py"):
        return {"sandbox_status": "Not Supported", "sandbox_output": "", "sandbox_error": "", "sandbox_disclaimer": "Sandbox execution testing currently only supports Python files. This file was not run - do not interpret this as a pass or fail."}
    import subprocess as _sp
    import tempfile as _tf
    import os as _os
    try:
        with _tf.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
            tmp.write(migrated_code)
            tmp_path = tmp.name
        try:
            result = _sp.run(["python3", tmp_path], timeout=8, capture_output=True, text=True)
            status = "Ran successfully" if result.returncode == 0 else "Ran with errors"
            output = (result.stdout or "")[:1000]
            err = (result.stderr or "")[:1000]
        except _sp.TimeoutExpired:
            status = "Timeout - execution took longer than 8 seconds"
            output = ""
            err = "Execution exceeded time limit"
        finally:
            try:
                _os.remove(tmp_path)
            except Exception:
                pass
        return {"sandbox_status": status, "sandbox_output": output, "sandbox_error": err, "sandbox_disclaimer": "This is a lightweight, resource-limited test run on the server, not a fully isolated Docker sandbox. Network and filesystem isolation are not yet in place. Use only with trusted, already-migrated code. A fully isolated sandbox is on the roadmap."}
    except Exception as e:
        return {"sandbox_status": "Sandbox test failed safely", "sandbox_error": str(e), "sandbox_output": "", "sandbox_disclaimer": "Lightweight sandbox test - full isolation planned for a future release."}'''

new = '''def run_sandboxed_migration_test(migrated_code, filename):
    return {"sandbox_status": "Disabled", "sandbox_output": "", "sandbox_error": "", "sandbox_disclaimer": "Sandboxed execution has been disabled: it previously ran uploaded code directly on the server process with only a timeout as protection (no network/filesystem isolation), which is a genuine remote-code-execution risk for a public-facing service. This feature will return once a properly isolated execution environment (e.g. a locked-down container with no network access, non-root user, and resource limits) is in place."}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")