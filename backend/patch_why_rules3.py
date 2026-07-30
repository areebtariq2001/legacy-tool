with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = 161
end_idx = 170

print("Line at start_idx (162):", repr(lines[161]))
print("Line at end boundary (170):", repr(lines[169]))
print("Line at end boundary (171):", repr(lines[170]))

new_block = []
new_block.append("\n")
new_block.append("JAVA_WHY_RULES = [\n")
new_block.append('    ("Vector", "Vector is a legacy synchronized collection from Java 1.0. ArrayList is preferred unless thread-safety is specifically required."),\n')
new_block.append('    ("Hashtable", "Hashtable is a legacy synchronized map. HashMap or ConcurrentHashMap is the modern equivalent."),\n')
new_block.append('    ("StringBuffer", "StringBuffer is synchronized and slower than StringBuilder. Use StringBuilder unless multiple threads mutate the same instance."),\n')
new_block.append('    ("System.out.println", "Direct println calls are hard to control in production. A logging framework such as SLF4J allows log levels and centralized output."),\n')
new_block.append("]\n")
new_block.append("\n")
new_block.append("PHP_WHY_RULES = [\n")
new_block.append('    ("mysql_", "The mysql_ extension was removed in PHP 7. mysqli or PDO should be used instead, and both support prepared statements which also prevent SQL injection."),\n')
new_block.append('    ("each(", "each() was removed in PHP 8. Use a foreach loop instead, which is simpler and faster."),\n')
new_block.append('    ("create_function", "create_function() was removed in PHP 8 due to security risks. Use an anonymous function (closure) instead."),\n')
new_block.append("]\n")
new_block.append("\n")
new_block.append("COBOL_WHY_RULES = [\n")
new_block.append('    ("GO TO", "GO TO creates unstructured control flow that is difficult to trace and migrate automatically."),\n')
new_block.append('    ("REDEFINES", "REDEFINES reinterprets the same memory as a different data type, which has no direct equivalent in modern languages."),\n')
new_block.append('    ("ALTER", "The ALTER statement dynamically changes a GO TO target at runtime and needs manual review to convert safely."),\n')
new_block.append("]\n")
new_block.append("\n")
new_block.append("def get_why_explanations(original_source, language=\"python\"):\n")
new_block.append("    explanations = []\n")
new_block.append('    if language == "python":\n')
new_block.append('        if "print " in original_source and not "print(" in original_source.split("print ")[0][-5:]:\n')
new_block.append('            explanations.append({"change": "print statement -> print()", "why": "In Python 3, print is a function, not a statement. It must be called with parentheses, e.g. print(x)."})\n')
new_block.append("        for keyword, reason in WHY_RULES:\n")
new_block.append("            if keyword in original_source:\n")
new_block.append('                explanations.append({"change": keyword, "why": reason})\n')
new_block.append('    elif language == "java":\n')
new_block.append("        for keyword, reason in JAVA_WHY_RULES:\n")
new_block.append("            if keyword in original_source:\n")
new_block.append('                explanations.append({"change": keyword, "why": reason})\n')
new_block.append('    elif language == "php":\n')
new_block.append("        for keyword, reason in PHP_WHY_RULES:\n")
new_block.append("            if keyword in original_source:\n")
new_block.append('                explanations.append({"change": keyword, "why": reason})\n')
new_block.append('    elif language == "cobol":\n')
new_block.append("        for keyword, reason in COBOL_WHY_RULES:\n")
new_block.append("            if keyword.upper() in original_source.upper():\n")
new_block.append('                explanations.append({"change": keyword, "why": reason})\n')
new_block.append("    return explanations\n")
new_block.append("\n")

lines[start_idx:end_idx] = new_block

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("PATCHED SUCCESSFULLY")