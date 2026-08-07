with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old_verdict = '''    if findings:
        verdict = "Weak or quantum-vulnerable cryptography detected"
    else:
        verdict = "No obvious weak cryptography detected"'''
new_verdict = '''    _high_count = sum(1 for f in findings if f["severity"] == "High")
    if _high_count > 0:
        verdict = "CRITICAL: " + str(_high_count) + " broken algorithm(s) found - immediate replacement required"
    elif findings:
        verdict = "WARNING: Quantum-vulnerable crypto detected - plan PQC migration"
    else:
        verdict = "No obvious weak cryptography detected"'''

old_patterns_end = '''(r"(?i)\\bDiffie[-\\s]?Hellman\\b", "Diffie-Hellman - quantum-vulnerable key exchange", "Medium"'''

count_verdict = content.count(old_verdict)
count_patterns = content.count(old_patterns_end)
print("Verdict occurrences:", count_verdict)
print("Patterns-end occurrences:", count_patterns)

if count_verdict == 1:
    content = content.replace(old_verdict, new_verdict, 1)
    print("Verdict PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED (step 1)")