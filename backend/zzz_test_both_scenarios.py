import main

# Scenario 1: Lambda call should genuinely NOW be captured
source1 = '''def calculate_interest(balance):
    return balance * 0.05

def fraud_score(txn):
    check = lambda x: calculate_interest(x)
    return check(txn)'''
result1 = main.analyze_call_graph(source1)

# Scenario 2: Original false-positive bug should genuinely STILL be fixed
# (nested NAMED function should NOT be wrongly attributed to outer function)
source2 = '''def calculate_interest(balance):
    return balance * 0.05

def outer_func():
    def inner_helper():
        return calculate_interest(100)
    return inner_helper()'''
result2 = main.analyze_call_graph(source2)

with open("zzz_both_output.txt", "w") as f:
    f.write("SCENARIO 1 (lambda) calls_map: " + str(result1["calls_map"]) + "\n")
    f.write("SCENARIO 2 (nested named func) calls_map: " + str(result2["calls_map"]) + "\n")

print("DONE")