import main

test_code = '''def get_user(user_id):
    sql = "SELECT * FROM customers WHERE id = " + user_id
    return sql'''

result = main.scan_sql_injection(test_code, "test.py")
for issue in result["sqli_issues"]:
    print("Line:", issue["line"])
    print("Likely source variable:", issue["likely_source_variable"])
    print("Evidence:", issue["evidence"])