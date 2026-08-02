import main

original_p2 = '''def calculate_interest(principal, rate, years):
    return principal * rate * years / 100
def check_balance(account_number, amount):
    print "checking"
    return True'''

migrated_p3 = '''def calculate_interest(principal, rate, years):
    return principal * rate * years / 100
def check_balance(account_number, amount):
    print("checking")
    return True'''

result = main.check_parity(original_p2, migrated_p3)
print("Original functions:", result["original_functions"])
print("Migrated functions:", result["migrated_functions"])
print("Parity OK:", result["parity_ok"])
print("Verdict:", result["parity_verdict"])