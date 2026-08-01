import main

bank_legacy_code = '''# Legacy banking module - Python 2
import datetime
def calculate_interest(principal, rate, years):
    simple_interest = (principal * rate * years) / 100
    return simple_interest
def check_balance(account_number, amount):
    min_balance = 1000
    available_balance = get_balance(account_number)
    if available_balance - amount < min_balance:
        print "Insufficient balance"
        return False
    return True
def get_balance(acc):
    return 5000'''

result = main.analyze_code(bank_legacy_code)
print("Functions found:", result["functions"])
print("AST parse failed:", result.get("ast_parse_failed"))
print("Issues:")
for issue in result["issues"]:
    print(" -", issue)