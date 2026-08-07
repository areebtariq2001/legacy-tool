import main

test_code = '''def calculate_interest(principal, rate):
    return principal * rate / 100

def fraud_score(txn):
    check = lambda x: calculate_interest(x, 5)
    if txn.amount > 1000:
        return "high"
    else:
        return "low"'''

result = main.analyze_call_graph(test_code)
print("calls_map:", result["calls_map"])