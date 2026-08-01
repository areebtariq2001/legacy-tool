import main

result1 = main.analyze_code('exec(some_code)')
result2 = main.analyze_code('exec some_code')

exec_issues_1 = [i for i in result1.get("issues", []) if "exec" in i.lower()]
exec_issues_2 = [i for i in result2.get("issues", []) if "exec" in i.lower()]

print("exec(x) - genuine Python 3, issues:", exec_issues_1)
print("exec x - genuine Python 2, issues:", exec_issues_2)