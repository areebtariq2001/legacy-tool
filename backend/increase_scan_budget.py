with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''_time_budget_seconds = 90'''
new1 = '''_time_budget_seconds = 180'''
c1 = content.count(old1)
print("Time-budget-occurrences:", c1)
if c1 == 1:
    content = content.replace(old1, new1, 1)

old2 = '''"disclaimer": "Scans up to 25 Python files from a public GitHub repo (free-tier limit). Each file is risk-assessed. Only Python files are currently supported - Java/PHP/COBOL repo-scanning is not yet available. For full/large repos, a paid server and deeper analysis are planned."'''
new2 = '''"disclaimer": "Scans Python files from a public GitHub repo within a 3-minute processing budget (free-tier limit, roughly 40-50 typical files). Each file is risk-assessed. Only Python files are currently supported - Java/PHP/COBOL repo-scanning is not yet available. For full/large repos, a paid server and deeper analysis are planned."'''
c2 = content.count(old2)
print("Disclaimer-occurrences:", c2)
if c2 == 1:
    content = content.replace(old2, new2, 1)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("SCAN-BUDGET-INCREASE-COMPLETED")