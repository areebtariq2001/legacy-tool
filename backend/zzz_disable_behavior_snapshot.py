with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def generate_behavior_snapshot(original_code, migrated_code, filename):
    if not filename.lower().endswith(".py"):
        return {"snapshot_status": "Not Supported", "match": None, "snapshot_disclaimer": "Characterization testing currently only supports Python files. This comparison was not run."}
    original_result = _run_single_sandbox(original_code)
    migrated_result = _run_single_sandbox(migrated_code)
    outputs_match = (original_result["stdout"] == migrated_result["stdout"])
    both_ran_ok = (original_result["returncode"] == 0 and migrated_result["returncode"] == 0)
    if not both_ran_ok:
        verdict = "Could not compare - one or both versions failed to run"
    elif outputs_match:
        verdict = "Behavior matches - same output produced"
    else:
        verdict = "Behavior differs - outputs are NOT identical, review required"
    return {"snapshot_status": "Compared", "match": outputs_match if both_ran_ok else None, "verdict": verdict, "original_run": {"ran_ok": original_result["returncode"] == 0, "output": original_result["stdout"], "error": original_result["stderr"]}, "migrated_run": {"ran_ok": migrated_result["returncode"] == 0, "output": migrated_result["stdout"], "error": migrated_result["stderr"]}, "snapshot_disclaimer": "Runs both versions with no input arguments in a lightweight, resource-limited sandbox (not fully isolated Docker) and compares their printed output. Functions requiring input or side effects (files, network, DB) are not captured. A starting signal, not a full behavioral guarantee."}'''

new = '''def generate_behavior_snapshot(original_code, migrated_code, filename):
    return {"snapshot_status": "Disabled", "match": None, "verdict": "Behavioral comparison is disabled", "snapshot_disclaimer": "This feature has been disabled: it previously executed both the original and migrated code directly on the server process with only a timeout as protection (no network/filesystem isolation), which is a genuine remote-code-execution risk for a public-facing service. It will return once a properly isolated execution environment is in place."}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")