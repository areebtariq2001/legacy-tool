with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '(r"(?i)[\\w-]*(password|passwd|pwd)[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x27\\x22][^\\x27\\x22]{2,}[\\x27\\x22]", "Hardcoded password (COBOL VALUE clause)", "High"),'
new1 = old1 + ' (r"(?i)MOVE\\s+[\\x27\\x22][^\\x27\\x22]{2,}[\\x27\\x22]\\s+TO\\s+[\\w-]*(PASSWORD|PASSWD|PWD)[\\w-]*", "Hardcoded password (COBOL MOVE statement)", "High"),'

old2 = '(r"(?i)[\\w-]*(password|passwd|pwd)[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\"\\x27][^\\"\\x27]{2,}[\\"\\x27]", "Hardcoded password (COBOL VALUE clause)"),'
new2 = old2 + ' (r"(?i)MOVE\\s+[\\"\\x27][^\\"\\x27]{2,}[\\"\\x27]\\s+TO\\s+[\\w-]*(PASSWORD|PASSWD|PWD)[\\w-]*", "Hardcoded password (COBOL MOVE statement)"),'

count1 = content.count(old1)
count2 = content.count(old2)
print("Pattern-1 occurrences:", count1)
print("Pattern-2 occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Pattern-1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Pattern-2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")