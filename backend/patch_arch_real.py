with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    except Exception:
        if filename.lower().endswith((".java",".php",".cbl",".cob")):
            if filename.lower().endswith(".php"):
                funcs = _re.findall(r"function\s+(\w+)\s*\([^)]*\)", source)
            else:
                funcs = _re.findall(r"(?:public|private|protected)\s+(?:static\s+)?(?:synchronized\s+)?[\w<>\[\]]+\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{", source)
            classes = _re.findall(r"\bclass\s+(\w+)", source)
            imports = _re.findall(r"import\s+([\w\.\*]+);", source)
        else:'''

new = '''    except Exception:
        if filename.lower().endswith((".cbl", ".cob")):
            funcs = _re.findall(r"(?m)^\s{0,7}([\w-]+)\.\s*$", source)
            classes = []
            imports = []
        elif filename.lower().endswith((".java",".php")):
            if filename.lower().endswith(".php"):
                funcs = _re.findall(r"function\s+(\w+)\s*\([^)]*\)", source)
            else:
                funcs = _re.findall(r"(?:public|private|protected)\s+(?:static\s+)?(?:synchronized\s+)?[\w<>\[\]]+\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{", source)
            classes = _re.findall(r"\bclass\s+(\w+)", source)
            imports = _re.findall(r"import\s+([\w\.\*]+);", source)
        else:'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT - need to inspect manually")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY - THIS TIME THE RIGHT FUNCTION")