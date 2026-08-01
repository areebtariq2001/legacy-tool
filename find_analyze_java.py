with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("analyze_java_check.txt", "w", encoding="utf-8") as out:
    out.write("analyze_java has scan_sql_injection: " + str("scan_sql_injection" in content.split("def analyze_java(")[1].split("def ")[0] if "def analyze_java(" in content else "N/A") + "\n")
    out.write("analyze_java has password regex: " + str("password" in content.split("def analyze_java(")[1].split("def ")[0].lower() if "def analyze_java(" in content else "N/A") + "\n")

print("DONE")