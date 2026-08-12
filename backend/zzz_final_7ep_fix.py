with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
r1 = ('        return {"filename": file.filename, "error": "Cost estimation failed safely: " + str(e)}', '        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Cost estimation failed safely: {e}"})')
r2 = ('        result = analyze_vendor_lockin(source, file.filename)\n        result["filename"] = file.filename\n        track_usage("vendor-lockin", file.filename)\n        return result\n    except Exception as e:\n        return {"filename": file.filename, "error": "Vendor lock-in analysis failed safely: " + str(e)}', '        result = analyze_vendor_lockin(source, file.filename)\n        result["filename"] = file.filename\n        track_usage("vendor-lockin", file.filename)\n        write_audit_log("vendor-lockin", file.filename, "findings=" + str(len(result.get("lockin_findings", []))))\n        return result\n    except Exception as e:\n        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Vendor lock-in analysis failed safely: {e}"})')
r3 = ('        result = score_zero_trust(source, file.filename)\n        result["filename"] = file.filename\n        track_usage("zero-trust-score", file.filename)\n        return result\n    except Exception as e:\n        return {"filename": file.filename, "error": "Zero-trust scoring failed safely: " + str(e)}', '        result = score_zero_trust(source, file.filename)\n        result["filename"] = file.filename\n        track_usage("zero-trust-score", file.filename)\n        write_audit_log("zero-trust-score", file.filename, "score=" + str(result.get("zt_score", 0)))\n        return result\n    except Exception as e:\n        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Zero-trust scoring failed safely: {e}"})')
total = 0
for old, new in [r1, r2, r3]:
    if content.count(old) == 1:
        content = content.replace(old, new, 1)
        total = total + 1
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
msg = "DONE total=" + str(total)
print(msg)