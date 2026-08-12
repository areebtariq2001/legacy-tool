with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        return {"filename": file.filename, "error": "Executive report failed safely: " + str(e)}'''
new1 = '''        return {"filename": file.filename, "error": f"Executive report failed safely: {e}"}'''

old2 = '''        result = analyze_impact(source, file.filename)
        result["filename"] = file.filename
        track_usage("analyze-impact", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Impact analysis failed safely: " + str(e)}'''
new2 = '''        result = analyze_impact(source, file.filename)
        result["filename"] = file.filename
        track_usage("analyze-impact", file.filename)
        write_audit_log("analyze-impact", file.filename, f"functions={len(result.get('impact_map', []))}")
        return result
    except Exception as e:
        return {"filename": file.filename, "error": f"Impact analysis failed safely: {e}"}'''

old3 = '''        result = map_transaction_flow(source, file.filename)
        result["filename"] = file.filename
        track_usage("map-transaction-flow", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Transaction flow mapping failed safely: " + str(e)}'''
new3 = '''        result = map_transaction_flow(source, file.filename)
        result["filename"] = file.filename
        track_usage("map-transaction-flow", file.filename)
        write_audit_log("map-transaction-flow", file.filename, f"flows={len(result.get('transaction_flows', []))}")
        return result
    except Exception as e:
        return {"filename": file.filename, "error": f"Transaction flow mapping failed safely: {e}"}'''

old4 = '''        result = generate_rollback_plan(source, file.filename)
        result["filename"] = file.filename
        track_usage("rollback-plan", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Rollback plan failed safely: " + str(e)}'''
new4 = '''        result = generate_rollback_plan(source, file.filename)
        result["filename"] = file.filename
        track_usage("rollback-plan", file.filename)
        write_audit_log("rollback-plan", file.filename, f"steps={len(result.get('rollback_steps', []))}")
        return result
    except Exception as e:
        return {"filename": file.filename, "error": f"Rollback plan failed safely: {e}"}'''

replacements = [(old1,new1),(old2,new2),(old3,new3),(old4,new4)]
total = 0
with open("zzz_5ep_fix_log.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(str(count) + " : " + old[:50] + "\n")
        if count == 1:
            content = content.replace(old, new, 1)
            total += 1

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("DONE - total patched:", total, "of 4")