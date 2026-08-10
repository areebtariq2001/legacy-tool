import importlib
import main
importlib.reload(main)

test_code = '''def calculate_interest(balance):
    return balance * 0.05

def fraud_score(txn):
    check = lambda x: calculate_interest(x)
    return check(txn)'''

result = main.analyze_call_graph(test_code)
print("FINAL genuinely-verified calls_map:", result["calls_map"])