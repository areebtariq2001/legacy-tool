import main

main.write_audit_log("test-action", "test-file.py", "test-summary")
print("_in_memory_audit_log[0]:", main._in_memory_audit_log[0])
print("Type:", type(main._in_memory_audit_log[0]))