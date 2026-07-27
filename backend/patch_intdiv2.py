with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = "    if re.search(r'except\\s+(\\w+)\\s*,\\s*(\\w+)', migrated):\n        migrated = re.sub(r'except\\s+(\\w+)\\s*,\\s*(\\w+)', r'except \\1 as \\2', migrated)\n        changes.append(\"except X, e -> except X as e\")\n    return {\"migrated_code\": migrated, \"changes\": changes, \"why_explanations\": get_why_explanations(source), \"dependencies\": check_dependencies(source)}"
new = "    if re.search(r'except\\s+(\\w+)\\s*,\\s*(\\w+)', migrated):\n        migrated = re.sub(r'except\\s+(\\w+)\\s*,\\s*(\\w+)', r'except \\1 as \\2', migrated)\n        changes.append(\"except X, e -> except X as e\")\n    _div_lines = [str(_i + 1) for _i, _ln in enumerate(migrated.split(chr(10))) if re.search(r'[\\w\\)\\]]\\s*/\\s*[\\w\\(]', _ln) and '//' not in _ln and not _ln.strip().startswith('#')]\n    if _div_lines:\n        changes.append(\"REVIEW NEEDED: Division (/) found on line(s) \" + \", \".join(_div_lines) + \" - Python 2 used floor division on integers, Python 3 uses true division. Verify this calculation still produces the intended result, especially for financial/numeric logic.\")\n    return {\"migrated_code\": migrated, \"changes\": changes, \"why_explanations\": get_why_explanations(source), \"dependencies\": check_dependencies(source)}"
count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")