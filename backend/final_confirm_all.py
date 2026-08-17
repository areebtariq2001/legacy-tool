import main
import inspect
with open("final_confirm_result.txt", "w", encoding="utf-8") as out:
    for r in main.app.routes:
        if hasattr(r, "endpoint") and r.endpoint.__name__ == "cross_language_migrate_endpoint":
            src = inspect.getsource(r.endpoint)
            out.write("=== cross_language_migrate_endpoint ===\n" + src + "\n\n")
            out.write("HAS-MAX-FILE-SIZE-CHECK: " + str("MAX_FILE_SIZE" in src) + "\n\n")
        if hasattr(r, "endpoint") and r.endpoint.__name__ == "github_issue_fix_endpoint":
            src2 = inspect.getsource(r.endpoint)
            out.write("=== github_issue_fix_endpoint ===\n" + src2 + "\n\n")
            out.write("HAS-NONE-SAFETY: " + str('or ""' in src2))
print("FINAL-CONFIRM-COMPLETED")