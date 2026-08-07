with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)\\b(risk[_\\s]?score|risk[_\\s]?rating|risk[_\\s]?category)\\b", "Customer risk scoring", "KYC"'''

import re as _re
matches = _re.findall(_re.escape(old) + r'.{0,80}', content)
print("Matches found:", len(matches))
if matches:
    print("Sample:", matches[0])