main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''        result["filename"] = file.filename
        track_usage("analyze", file.filename)
        write_audit_log("analyze", file.filename, f"issues={len(result.get('issues', []))}")
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"filename": file.filename, "error": f"Analysis failed safely: {str(e)}"})'''

new = '''        result["filename"] = file.filename
        track_usage("analyze", file.filename)
        write_audit_log("analyze", file.filename, f"issues={len(result.get('issues', []))}")
        try:
            store_analyzed_file(file.filename, source)
        except Exception:
            pass
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"filename": file.filename, "error": f"Analysis failed safely: {str(e)}"})'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("STORE-WIRED-INTO-ANALYZE")
else:
    print("FAILED - count was:", count)