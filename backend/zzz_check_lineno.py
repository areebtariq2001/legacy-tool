import main

with open("zzz_lineno_output.txt", "w") as f:
    f.write("Actual bound function line: " + str(main.analyze_call_graph.__code__.co_firstlineno) + "\n")

with open("main.py", "r", encoding="utf-8") as mf:
    lines = mf.readlines()

matches = [i+1 for i, l in enumerate(lines) if "def analyze_call_graph" in l]
with open("zzz_lineno_output.txt", "a") as f:
    f.write("All 'def analyze_call_graph' occurrences at lines: " + str(matches) + "\n")

print("DONE")