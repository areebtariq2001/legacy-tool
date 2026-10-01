import os
import glob

root_dir = r"C:\Users\dell\Desktop\legacy-migration-tool"
backend_dir = os.path.join(root_dir, "backend")

patterns = [
    "find_*.py", "find_*.txt", "verify_*.py", "verify_*.txt",
    "test_*.py", "test_*.txt", "implement_*.py", "implement_*.txt",
    "investigate_*.py", "investigate_*.txt", "get_*.py", "get_*.txt",
    "add_*.py", "add_*.txt", "fix_*.py", "fix_*.txt",
    "check_*.py", "check_*.txt", "reverify_*.py", "reverify_*.txt",
    "harden_*.py", "harden_*.txt", "wire_*.py", "wire_*.txt",
    "revert_*.py", "revert_*.txt", "sample_*.py", "sample_*.txt",
    "self_audit_*.py", "self_audit_*.txt", "cleanup_temp_files*.py",
]

protected = {"main.py", "requirements.txt", "test_starsage.py", "test_regex_patterns.py"}

deleted_count = 0
for directory in [root_dir, backend_dir]:
    for pattern in patterns:
        for filepath in glob.glob(os.path.join(directory, pattern)):
            filename = os.path.basename(filepath)
            if filename in protected or filename == "cleanup_temp_files2.py":
                continue
            try:
                os.remove(filepath)
                deleted_count += 1
            except Exception as e:
                print("Could not delete:", filepath, "-", e)

print("Genuinely deleted", deleted_count, "temporary files.")
print("CLEANUP-2-COMPLETE")