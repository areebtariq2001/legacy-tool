import main

test_sql = '''def get_customer(customer_id):
    query = "SELECT * FROM customers WHERE id = '%s'" % customer_id
    return query'''

test_cmd = '''def run_command(cmd):
    os.system("echo " + cmd)
    return True'''

result_sql = main.scan_sql_injection(test_sql, "test.py")
print("SQL injection findings:", result_sql["sqli_issues"])

# Check for command injection pattern in SENSITIVE_PATTERNS
result_sens = main.scan_sensitive_data(test_cmd)
print("Sensitive-data findings for cmd-injection:", [f["issue"] for f in result_sens["findings"]])