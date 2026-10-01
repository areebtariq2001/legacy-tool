main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: scan_entropy_secrets high_count should use findings_full
old1 = 'high_count = sum(1 for f in findings if f["confidence"] == "High")'
new1 = 'high_count = sum(1 for f in findings_full if f["confidence"] == "High")'
results["1_entropy_high_count"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: process_github_webhook PR files - capture full count
old2 = '                    if _pr_resp.status_code == 200:\n                        for _pf in _pr_resp.json()[:20]:'
new2 = '                    if _pr_resp.status_code == 200:\n                        _all_pr_files = _pr_resp.json()\n                        _total_pr_files_detected = len(_all_pr_files)\n                        for _pf in _all_pr_files[:20]:'
results["2_pr_files_capture"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: process_github_webhook changed_files - capture full count and add transparency fields
old3 = '        results = []\n        _webhook_scan_start = time.time()\n        _webhook_time_budget = 60\n        for file_path in list(changed_files)[:10]:'
new3 = '        results = []\n        _webhook_scan_start = time.time()\n        _webhook_time_budget = 60\n        _changed_files_full = list(changed_files)\n        _files_to_scan = _changed_files_full[:10]\n        for file_path in _files_to_scan:'
results["3_changed_files_capture"] = content.count(old3)
content = content.replace(old3, new3, 1)

old3b = '        high_risk = len([r for r in results if r.get("risk_level") == "High"])\n        return {"repo": repo_name, "pusher": pusher, "ref": ref, "trigger_type": "pull_request" if _is_pr_event else "push", "files_scanned": len(results),'
new3b = '        high_risk = len([r for r in results if r.get("risk_level") == "High"])\n        return {"repo": repo_name, "pusher": pusher, "ref": ref, "trigger_type": "pull_request" if _is_pr_event else "push", "files_scanned": len(results), "total_changed_files_detected": len(_changed_files_full), "files_not_scanned_this_run": max(0, len(_changed_files_full) - len(_files_to_scan)),'
results["3b_changed_files_use"] = content.count(old3b)
content = content.replace(old3b, new3b, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXWEBHOOK-DONE")