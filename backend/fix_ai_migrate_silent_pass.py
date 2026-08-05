with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            try:
                result.update(check_parity(source, result.get("migrated_code", "")))
                result.update(generate_test_scenarios(source, file.filename))
                result.update(generate_dockerfile(file.filename, detect_language(file.filename)))
            except Exception:
                pass'''

new = '''            try:
                result.update(check_parity(source, result.get("migrated_code", "")))
            except Exception as e:
                result["parity_ok"] = None
                result["parity_error"] = "Parity check failed: " + str(e)
            try:
                result.update(generate_test_scenarios(source, file.filename))
            except Exception as e:
                result["test_scenarios_error"] = "Test scenario generation failed: " + str(e)
            try:
                result.update(generate_dockerfile(file.filename, detect_language(file.filename)))
            except Exception as e:
                result["dockerfile_error"] = "Dockerfile generation failed: " + str(e)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")