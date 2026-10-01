main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    except Exception as e:
        return {"success": False, "error": f"Login failed: {e}"}
    finally:
        if cur:'''
new = '''    except Exception as e:
        write_audit_log("login-error", email, str(e))
        return {"success": False, "error": "Login failed - please try again shortly"}
    finally:
        if cur:'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSTRELEAK-DONE")
else:
    print("FAILED - count was:", count)