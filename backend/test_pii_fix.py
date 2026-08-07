import main

test_code = '''def check_balance(account_number, amount):
    available_balance = get_balance(account_number)

def process_transaction(account_number, amount, txn_type):
    debit(account_number, amount)
    credit(account_number, amount)
    log_transaction(account_number, amount, txn_type)'''

result = main.detect_pii(test_code, "test.py")
print("PII findings:", result["pii_findings"])
print("pii_clean:", result["pii_clean"])