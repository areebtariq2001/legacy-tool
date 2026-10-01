main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if _ai_lang == "python" and result.get("migrated_code"):
            try:
                result.update(check_parity(source, result.get("migrated_code", "")))
            except Exception as e:
                result["parity_ok"] = None
                result["parity_error"] = f"Parity check failed: {e}"
            try:
                result.update(generate_test_scenarios(source, file.filename))
            except Exception as e:
                result["test_scenarios_error"] = f"Test scenario generation failed: {e}"
            try:
                result.update(generate_dockerfile(file.filename, _ai_lang))
            except Exception as e:
                result["dockerfile_error"] = f"Dockerfile generation failed: {e}"'''

new = '''        if _ai_lang == "python" and result.get("migrated_code"):
            try:
                result.update(check_parity(source, result.get("migrated_code", "")))
            except Exception as e:
                result["parity_ok"] = None
                result["parity_error"] = f"Parity check failed: {e}"
            try:
                result.update(generate_test_scenarios(source, file.filename))
            except Exception as e:
                result["test_scenarios_error"] = f"Test scenario generation failed: {e}"
        if result.get("migrated_code"):
            try:
                result.update(generate_dockerfile(file.filename, _ai_lang))
            except Exception as e:
                result["dockerfile_error"] = f"Dockerfile generation failed: {e}"'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("DOCKERFILE-EXTENDED-ALL-LANGS")
else:
    print("FAILED - count was:", count)