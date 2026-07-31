with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        try:
            fallback_output.update(compare_complexity(source, rule_result["migrated_code"]))
        except Exception:
            pass
        return fallback_output'''

new1 = '''        try:
            fallback_output.update(compare_complexity(source, rule_result["migrated_code"]))
        except Exception as e:
            print("Warning: compare_complexity failed in ai_advanced_migrate fallback: " + str(e))
        return fallback_output'''

old2 = '''        try:
            output.update(compare_complexity(source, output.get("migrated_code", source)))
        except Exception:
            pass
        output["why_explanations"] = get_why_explanations(source)'''

new2 = '''        try:
            output.update(compare_complexity(source, output.get("migrated_code", source)))
        except Exception as e:
            print("Warning: compare_complexity failed in ai_advanced_migrate: " + str(e))
        output["why_explanations"] = get_why_explanations(source)'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Fix 1 occurrences:", count1)
print("Fix 2 occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Fix 1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix 2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")