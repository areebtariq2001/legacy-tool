main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: score=90 fallback (Python path)
old1 = '"confidence_score": 90, "confidence_level": "High confidence", "confidence_reason":'
new1 = '"confidence_score": 40, "confidence_level": "Low confidence - AI failed, rule-based fallback used, manual review required", "confidence_reason":'
results["1_score90"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2 and 3: score=95 fallback (appears twice, identical text - Java/PHP paths)
old2 = '''output["confidence_score"] = 95
                output["confidence_level"] = "High confidence"
                output["confidence_reason"] = "AI output was unreliable; switched to deterministic rule-based migration"'''
new2 = '''output["confidence_score"] = 40
                output["confidence_level"] = "Low confidence - AI failed, rule-based fallback used, manual review required"
                output["confidence_reason"] = "AI output was unreliable; switched to deterministic rule-based migration"'''
count_before = content.count(old2)
content = content.replace(old2, new2)  # replace ALL occurrences (both are identical and both need the same fix)
results["2_and_3_score95_both"] = count_before

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXFAKECONF-DONE")