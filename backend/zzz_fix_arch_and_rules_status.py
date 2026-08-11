with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        write_audit_log("generate-architecture", file.filename, f"layers={len(result.get('architecture_layers', []))}")
        return result
    except Exception as e:
        return {"filename": file.filename, "error": f"Architecture generation failed safely: {e}"}'''

new1 = '''        write_audit_log("generate-architecture", file.filename, f"layers={len(result.get('architecture_layers', []))}")
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Architecture generation failed safely: {e}"})'''

old2 = '''        if error:
            return {'filename': file.filename, 'error': error}
        result = extract_business_rules(source, detect_language(file.filename))'''

new2 = '''        if error:
            return JSONResponse(status_code=400, content={'filename': file.filename, 'error': error})
        result = extract_business_rules(source, detect_language(file.filename))'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Occurrences 1:", count1)
print("Occurrences 2:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("PATCHED 1")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("PATCHED 2")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")