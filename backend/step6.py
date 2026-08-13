with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

results = []

old_a = "        result = process_github_webhook(payload)\n        return result\n    except Exception as e:\n        return {\"error\": \"Webhook endpoint failed safely: \" + str(e)}"
new_a = "        result = process_github_webhook(payload)\n        track_usage(\"github-webhook\", \"webhook\")\n        return result\n    except Exception as e:\n        return JSONResponse(status_code=400, content={\"error\": \"Webhook endpoint failed safely: \" + str(e)})"
ca = content.count(old_a)
if ca == 1:
    content = content.replace(old_a, new_a, 1)
results.append("webhook: " + str(ca))

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step6_log.txt", "w") as log:
    log.write(chr(10).join(results))
print("STEP6 DONE")
