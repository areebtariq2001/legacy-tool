import main

with open("zzz_debug99.py", "r") as f:
    old_script = f.read()

source = '''def calculate_interest(balance):
    return balance * 0.05

def fraud_score(txn):
    check = lambda x: calculate_interest(x)
    return check(txn)'''

result = main.analyze_call_graph(source)

with open("zzz_final_output.txt", "w") as f:
    f.write("Source repr: " + repr(source) + "\n\n")
    f.write("Result: " + str(result) + "\n")

print("DONE")