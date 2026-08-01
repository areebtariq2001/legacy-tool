with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def analyze_php(source):
    issues = []
    if re.search(r"(?i)(password|passwd|pwd|api_key|secret)\\s*=\\s*[\\x22\\x27][^\\x22\\x27]{3,}[\\x22\\x27]", source):
        issues.append("Hardcoded password/credential found - move to environment variable")'''

new = '''def analyze_php(source):
    issues = []
    _source_no_comments = re.sub(r'//.*', '', source)
    _source_no_comments = re.sub(r'#.*', '', _source_no_comments)
    if re.search(r"(?i)(password|passwd|pwd|api_key|secret)\\s*=\\s*[\\x22\\x27][^\\x22\\x27]{3,}[\\x22\\x27]", _source_no_comments):
        issues.append("Hardcoded password/credential found - move to environment variable")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")