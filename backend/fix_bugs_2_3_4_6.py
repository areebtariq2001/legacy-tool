with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''(r"\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b", "Hardcoded IP address", "Medium"),'''
new1 = '''(r"\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b", "Hardcoded IP address", "Medium"),'''

old2 = '''(r"\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b", "Possible phone number", "Low"),'''
new2 = '''(r"(?<![\\d.])\\d{3}[-]\\d{3}[-]\\d{4}(?![\\d.])", "Possible phone number", "Low"),'''

old3 = '''(r"(?i)(execute|cursor\\.execute|query)\\s*\\(\\s*[\\x22\\x27].*%.*[\\x22\\x27]\\s*%", "Possible SQL injection (string formatting in query)", "High"),'''
new3 = old3 + '''
    (r"(?i)(execute|cursor\\.execute)\\s*\\(\\s*f[\\x22\\x27]", "SQL injection risk (f-string in query)", "High"),
    (r"(?i)(execute|cursor\\.execute)\\s*\\([^)]*\\.format\\s*\\(", "SQL injection risk (.format() in query)", "High"),'''

old4 = '''(r"http://[^\\s\\x22\\x27]+", "Insecure HTTP (non-TLS) URL", "Medium"),'''
new4 = '''(r"http://(?!localhost|127\\.0\\.0\\.1)[^\\s\\x22\\x27]+", "Insecure HTTP URL (non-localhost)", "Medium"),'''

count1 = content.count(old1)
count2 = content.count(old2)
count3 = content.count(old3)
count4 = content.count(old4)
print("Bug-2 (IP) occurrences:", count1)
print("Bug-3 (phone) occurrences:", count2)
print("Bug-4 (SQL f-string) occurrences:", count3)
print("Bug-6 (HTTP localhost) occurrences:", count4)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Bug-2 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Bug-3 PATCHED")
if count3 == 1:
    content = content.replace(old3, new3, 1)
    print("Bug-4 PATCHED")
if count4 == 1:
    content = content.replace(old4, new4, 1)
    print("Bug-6 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")