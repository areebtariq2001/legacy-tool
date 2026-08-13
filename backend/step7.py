with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "        track_usage(\"regulatory-framework\", file.filename)\n        return result\n    except Exception as e:\n        return {\"filename\": file.filename, \"error\": \"Regulatory framework check failed safely: \" + str(e)}"
new = "        track_usage(\"regulatory-framework\", file.filename)\n        write_audit_log(\"regulatory-framework\", file.filename, \"framework=\" + framework)\n        return result\n    except Exception as e:\n        return JSONResponse(status_code=400, content={\"filename\": file.filename, \"error\": \"Regulatory framework check failed safely: \" + str(e)})"
c = content.count(old)
with open("step7_log.txt", "w") as log:
    log.write("count: " + str(c))
if c == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
print("STEP7 DONE")
