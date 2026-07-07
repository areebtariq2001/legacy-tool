# Legacy banking module - Python 2
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

def process_transaction(account_number, amount, txn_type):
    if txn_type == "withdraw":
        debit(account_number, amount)
    elif txn_type == "deposit":
        credit(account_number, amount)
    log_transaction(account_number, amount, txn_type)

def loan_emi(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure
    return emi

def get_balance(acc):
    return 5000

def debit(acc, amt):
    pass

def credit(acc, amt):
    pass

def log_transaction(acc, amt, t):
    pass