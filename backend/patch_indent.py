with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '    indent = "    "'
new1 = '    if_depth = 0\n    def cur_indent():\n        return "    " * (1 + if_depth) if in_procedure else "    " * if_depth'

if old1 not in content:
    print("STEP1 FAILED - marker not found")
else:
    content = content.replace(old1, new1, 1)
    print("STEP1 OK")

old2 = '(indent if in_procedure else "")'
count2 = content.count(old2)
print("STEP2 occurrences:", count2)
content = content.replace(old2, "cur_indent()")

old3 = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = cond.replace(" = ", " == ")
            words = cond.split(" ")
            fixed_words = []
            for w in words:
                if w and w[0] not in (chr(34), chr(39)) and "-" in w and any(c.isalnum() for c in w):
                    fixed_words.append(w.replace("-", "_"))
                else:
                    fixed_words.append(w)
            cond = " ".join(fixed_words)
            out_lines.append(cur_indent() + "if " + cond + ":")
            changes.append("IF -> if (= converted to == and variable hyphens fixed)")
            continue'''

new3 = '''        if upper.rstrip(".") == "ELSE":
            if_depth = max(0, if_depth - 1)
            out_lines.append(cur_indent() + "else:")
            if_depth += 1
            changes.append("ELSE -> else")
            continue
        if upper.startswith("END-IF"):
            if_depth = max(0, if_depth - 1)
            changes.append("END-IF removed (Python uses indentation)")
            continue
        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = cond.replace(" = ", " == ")
            words = cond.split(" ")
            fixed_words = []
            for w in words:
                if w and w[0] not in (chr(34), chr(39)) and "-" in w and any(c.isalnum() for c in w):
                    fixed_words.append(w.replace("-", "_"))
                else:
                    fixed_words.append(w)
            cond = " ".join(fixed_words)
            out_lines.append(cur_indent() + "if " + cond + ":")
            if_depth += 1
            changes.append("IF -> if (= converted to == and variable hyphens fixed)")
            continue'''

if old3 not in content:
    print("STEP3 FAILED - marker not found")
else:
    content = content.replace(old3, new3, 1)
    print("STEP3 OK")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("ALL DONE")