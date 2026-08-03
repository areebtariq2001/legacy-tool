with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("END-IF"):
            if_depth = max(0, if_depth - 1)
            changes.append("END-IF removed (Python uses indentation)")
            continue'''

new = '''        if upper.startswith("END-IF"):
            if if_depth == 0:
                changes.append("REVIEW NEEDED: unexpected END-IF with no matching IF - the source COBOL may have mismatched IF/END-IF blocks. Indentation from this point onward may be incorrect - review the migrated output carefully.")
            if_depth = max(0, if_depth - 1)
            changes.append("END-IF removed (Python uses indentation)")
            continue'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")