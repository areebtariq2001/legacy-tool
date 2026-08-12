with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('''        result = detect_tech_stack(source, file.filename)
        result["filename"] = file.filename
        track_usage("detect-tech-stack", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Tech stack detection failed safely: " + str(e)}''',
     '''        result = detect_tech_stack(source, file.filename)
        result["filename"] = file.filename
        track_usage("detect-tech-stack", file.filename)
        write_audit_log("detect-tech-stack", file.filename, f"stacks={len(result.get('tech_stack', []))}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Tech stack detection failed safely: {e}"})'''),

    ('''        result = audit_key_management(source, file.filename)
        result["filename"] = file.filename
        track_usage("audit-keys", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Key audit failed safely: " + str(e)}''',
     '''        result = audit_key_management(source, file.filename)
        result["filename"] = file.filename
        track_usage("audit-keys", file.filename)
        write_audit_log("audit-keys", file.filename, "key audit completed")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Key audit failed safely: {e}"})'''),

    ('''        result = detect_fraud_gaps(source, file.filename)
        result["filename"] = file.filename
        track_usage("detect-fraud-gaps", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Fraud gap detection failed safely: " + str(e)}''',
     '''        result = detect_fraud_gaps(source, file.filename)
        result["filename"] = file.filename
        track_usage("detect-fraud-gaps", file.filename)
        write_audit_log("detect-fraud-gaps", file.filename, f"score={result.get('fraud_score', 0)}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Fraud gap detection failed safely: {e}"})'''),
]

total = 0
with open("zzz_7ep_fix_log1.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(str(count) + " : " + old[:50] + "\n")
        if count == 1:
            content = content.replace(old, new, 1)
            total += 1

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("DONE - total patched:", total, "of 3")