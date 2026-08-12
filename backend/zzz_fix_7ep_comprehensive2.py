with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('''        return {"filename": file.filename, "error": "Cost estimation failed safely: " + str(e)}''',
     '''        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Cost estimation failed safely: {e}"})'''),

    ('''async def regional_compliance_endpoint(file: UploadFile = File(...), region: str = "Pakistan"):
    try:
        content = await file.read()
        source, error = safe_read_file(content, file.filename)
        if error:
            return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
        result = map_regional_compliance(source, file.filename, region)
        result["filename"] = file.filename
        track_usage("regional-compliance", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Regional compliance mapping failed safely: " + str(e)}''',
     '''async def regional_compliance_endpoint(file: UploadFile = File(...), region: str = "Pakistan"):
    try:
        _allowed_regions = {"Pakistan", "Global"}
        if region not in _allowed_regions:
            return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Invalid region '{region}'. Allowed: {', '.join(_allowed_regions)}"})
        content = await file.read()
        source, error = safe_read_file(content, file.filename)
        if error:
            return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
        result = map_regional_compliance(source, file.filename, region)
        result["filename"] = file.filename
        track_usage("regional-compliance", file.filename)
        write_audit_log("regional-compliance", file.filename, f"region={region}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Regional compliance mapping failed safely: {e}"})'''),

    ('''        result = analyze_vendor_lockin(source, file.filename)
        result["filename"] = file.filename
        track_usage("vendor-lockin", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Vendor lock-in analysis failed safely: " + str(e)}''',
     '''        result = analyze_vendor_lockin(source, file.filename)
        result["filename"] = file.filename
        track_usage("vendor-lockin", file.filename)
        write_audit_log("vendor-lockin", file.filename, f"findings={len(result.get('lockin_findings', []))}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Vendor lock-in analysis failed safely: {e}"})'''),

    ('''        result = score_zero_trust(source, file.filename)
        result["filename"] = file.filename
        track_usage("zero-trust-score", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Zero-trust scoring failed safely: " + str(e)}''',
     '''        result = score_zero_trust(source, file.filename)
        result["filename"] = file.filename
        track_usage("zero-trust-score", file.filename)
        write_audit_log("zero-trust-score", file.filename, f"score={result.get('zt_score', 0)}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Zero-trust scoring failed safely: {e}"})'''),
]

total = 0
with open("zzz_7ep_fix_log2.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(str(count) + " : " + old[:50] + "\n")
        if count == 1:
            content = content.replace(old, new, 1)
            total += 1

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("DONE - total patched:", total, "of 4")d