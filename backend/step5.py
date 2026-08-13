with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = "        result = call_ollama(chr(34) + chr(83) + chr(97) + chr(121) + chr(32) + chr(79) + chr(75) + chr(32) + chr(105) + chr(102) + chr(32) + chr(121) + chr(111) + chr(117) + chr(32) + chr(97) + chr(114) + chr(101) + chr(32) + chr(119) + chr(111) + chr(114) + chr(107) + chr(105) + chr(110) + chr(103) + chr(46) + chr(34))"

results = []
idx_ollama = content.find("result = call_ollama(")
idx_end = content.find(chr(10), idx_ollama)
old1_actual = content[idx_ollama:idx_end]
new1_actual = old1_actual + chr(10) + "    write_audit_log(\"local-ai-status\", \"n/a\", \"checked\")"
c1 = content.count(old1_actual)
if c1 == 1:
    content = content.replace(old1_actual, new1_actual, 1)
    results.append("local-ai-status: patched")
else:
    results.append("local-ai-status: count=" + str(c1))

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step5_log.txt", "w") as log:
    log.write(chr(10).join(results))
print("STEP5 DONE")
