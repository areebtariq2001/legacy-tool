import subprocess

files_to_remove = [
    "backend/basic_test.py", "backend/bug4_precheck3.py", "backend/check156.py",
    "backend/clean_up_regex_check.py", "backend/compat_p1.py", "backend/compat_simple.py",
    "backend/decisive_platform_test.py", "backend/enhance_migration_plan2.py",
    "backend/final_callgraph_verify.py", "backend/final_check_seqre_mre.py",
    "backend/final_confirm_all.py", "backend/final_verify_severity.py",
    "backend/force_db_test.py", "backend/force_db_test2.py", "backend/fresh_count_check.py",
    "backend/increase_scan_budget.py", "backend/inspect_arch.py", "backend/inspect_hyphen.py",
    "backend/investigate_duplicates.py", "backend/protect_approval_endpoints.py",
    "backend/quick_fixes2.py", "backend/recheck_smells_current.py",
    "backend/remove_bad_import_line.py", "backend/remove_dangerous_helper.py",
    "backend/remove_dangerous_helper2.py", "backend/remove_dead_code.py",
    "backend/remove_duplicates.py", "backend/remove_duplicates2.py", "backend/revert_bug8.py",
    "backend/rewrite_strangler_fig.py", "backend/save_output.py", "backend/show_broken_lines.py",
    "backend/slice_living.py", "backend/step1.py", "backend/step2.py", "backend/step3.py",
    "backend/step4.py", "backend/step5.py", "backend/step6.py", "backend/step7.py",
    "backend/step8.py", "backend/step9.py", "backend/stress_test_cobol.py",
    "backend/stress_test_save.py", "backend/tighten_redos_patterns.py", "backend/tinytest.py",
    "backend/tinytest2.py", "test_runner.py",
]

removed = []
failed = []
for f in files_to_remove:
    result = subprocess.run(["git", "rm", "-f", f], capture_output=True, text=True)
    if result.returncode == 0:
        removed.append(f)
    else:
        failed.append(f)

result2 = subprocess.run(["git", "rm", "-rf", "test_files", "test_batch"], capture_output=True, text=True)

with open("cleanup_log.txt", "w", encoding="utf-8") as log:
    log.write("Removed: " + str(len(removed)) + " files\n")
    log.write("Failed: " + str(len(failed)) + "\n")
    for f in failed:
        log.write("FAILED: " + f + "\n")
    log.write("test_files/test_batch removal returncode: " + str(result2.returncode) + "\n")
    log.write(result2.stdout + result2.stderr)

print("CLEANUP-SCRIPT-COMPLETED - check cleanup_log.txt")