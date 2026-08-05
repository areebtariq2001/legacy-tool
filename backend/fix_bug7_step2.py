with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old_php = '''        _sqli_result = scan_sql_injection(source, "file.php")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    return {"issues": issues}'''
new_php = '''        _sqli_result = scan_sql_injection(source, "file.php")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    _php_funcs = list(dict.fromkeys(re.findall(r"function\\s+(\\w+)\\s*\\(", source)))
    _php_classes = list(dict.fromkeys(re.findall(r"\\bclass\\s+(\\w+)", source)))
    return {"issues": issues, "classes": _php_classes, "methods": _php_funcs[:20], "total_methods": len(_php_funcs), "methods_truncated": len(_php_funcs) > 20, "php_summary": str(len(_php_classes)) + " class(es), " + str(len(_php_funcs)) + " function(s) found"}'''

old_cobol = '''        _sqli_result = scan_sql_injection(source, "file.cbl")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    return {"issues": issues}'''
new_cobol = '''        _sqli_result = scan_sql_injection(source, "file.cbl")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    return {"issues": issues, "classes": [], "methods": _cobol_paras[:20], "total_methods": len(_cobol_paras), "methods_truncated": len(_cobol_paras) > 20, "cobol_summary": str(len(_cobol_paras)) + " paragraph(s) found (COBOL has no classes/OOP)"}'''

count_php = content.count(old_php)
count_cobol = content.count(old_cobol)
print("PHP occurrences:", count_php)
print("COBOL occurrences:", count_cobol)

if count_php == 1:
    content = content.replace(old_php, new_php, 1)
    print("PHP PATCHED")
if count_cobol == 1:
    content = content.replace(old_cobol, new_cobol, 1)
    print("COBOL PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")