import main
main.track_usage("analyze", "test_file.py")
main.write_audit_log("analyze", "test_file.py", "success")
print("No crash - track_usage and write_audit_log work locally with in-memory fallback")
print("Stats:", main.load_stats())