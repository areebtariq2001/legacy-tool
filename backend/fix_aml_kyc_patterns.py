with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''(r"(?i)\\b(aml|anti[_\\s]?money|launder|str|sar)\\b", "Anti-money-laundering logic", "AML"'''
new1 = '''(r"(?i)\\b(aml|anti[_\\s]?money|launder|suspicious[_\\s]?activity[_\\s]?report|str_filing|\\bsar_report)\\b", "Anti-money-laundering logic", "AML"'''

old2 = '''(r"(?i)\\b(pep|politically[_\\s]?exposed|due[_\\s]?diligence|edd|cdd)\\b", "Due diligence / PEP screening", "KYC"'''
new2 = '''(r"(?i)\\b(politically[_\\s]?exposed|due[_\\s]?diligence|\\bedd\\b|\\bcdd\\b|pep[_\\s]?screening|pep[_\\s]?check|pep[_\\s]?flag)\\b", "Due diligence / PEP screening", "KYC"'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Pattern-1 (str/sar) occurrences:", count1)
print("Pattern-2 (pep) occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Pattern-1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Pattern-2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")