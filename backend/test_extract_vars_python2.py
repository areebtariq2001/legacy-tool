import main

original_p2 = '''def check_balance(account_number, amount):
    min_balance = 1000
    available_balance = get_balance(account_number)
    if available_balance - amount < min_balance:
        print "Insufficient balance"
        return False
    return True'''

migrated_p3 = '''def check_balance(account_number, amount):
    min_balance = 1000
    available_balance = get_balance(account_number)
    if available_balance - amount < min_balance:
        print("Insufficient balance")
        return False
    return True'''

orig_vars = main.extract_variables(original_p2)
mig_vars = main.extract_variables(migrated_p3)
print("Original vars extracted:", orig_vars)
print("Migrated vars extracted:", mig_vars)

integrity_result = main.check_variable_integrity(original_p2, migrated_p3)
print("Integrity check result:", integrity_result)