import main

test_code = '''def get_customer(customer_id):
    query = "SELECT * FROM customers WHERE id = '%s'" % customer_id
    return query

def run_command(cmd):
    os.system("process_txn " + cmd)
    return True'''

result = main.analyze_code(test_code)
for issue in result["issues"]:
    print("-", issue)