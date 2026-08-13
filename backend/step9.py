with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "    result = call_ollama(\"Say OK if you are working.\")\n    is_working = \"not reachable\" not in result and not result.lower().startswith(\"error\")\n    return {\"local_ai_available\": is_working, \"response_preview\": result[:200], \"note\": \"Local AI runs on the same machine as the backend. In this cloud demo, the backend and your Ollama are on different machines, so this will show unavailable - it works fully in an on-premise deployment where both run together.\"}"
new = "    result = call_ollama(\"Say OK if you are working.\")\n    is_working = \"not reachable\" not in result and not result.lower().startswith(\"error\")\n    write_audit_log(\"local-ai-status\", \"n/a\", \"available=\" + str(is_working))\n    return {\"local_ai_available\": is_working, \"response_preview\": result[:200], \"note\": \"Local AI runs on the same machine as the backend. In this cloud demo, the backend and your Ollama are on different machines, so this will show unavailable - it works fully in an on-premise deployment where both run together.\"}"
c = content.count(old)
with open("step9_log.txt", "w") as log:
    log.write("count: " + str(c))
if c == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
print("STEP9 DONE")
