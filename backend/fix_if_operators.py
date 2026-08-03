with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = cond.replace(" = ", " == ")
            _words = cond.split(" ")
            _fixed_words = []
            for _w in _words:
                if _w and _w[0] not in (chr(34), chr(39)) and "-" in _w and any(_c.isalnum() for _c in _w):
                    _fixed_words.append(_w.replace("-", "_"))
                else:
                    _fixed_words.append(_w)
            cond = " ".join(_fixed_words)
            out_lines.append(cur_indent() + "if " + cond + ":")
            if_depth += 1
            changes.append("IF -> if (= converted to ==)")'''

new = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            _words = cond.split(" ")
            _fixed_words = []
            for _w in _words:
                if _w and _w[0] not in ('"', "'") and "-" in _w and any(_c.isalnum() for _c in _w):
                    _fixed_words.append(_w.replace("-", "_"))
                else:
                    _fixed_words.append(_w)
            cond = " ".join(_fixed_words)
            _cobol_ops = [
                (r"\\bGREATER\\s+THAN\\s+OR\\s+EQUAL\\s+TO\\b|\\bGREATER\\s+THAN\\s+OR\\s+EQUAL\\b", ">="),
                (r"\\bLESS\\s+THAN\\s+OR\\s+EQUAL\\s+TO\\b|\\bLESS\\s+THAN\\s+OR\\s+EQUAL\\b", "<="),
                (r"\\bGREATER\\s+THAN\\b", ">"),
                (r"\\bLESS\\s+THAN\\b", "<"),
                (r"\\bNOT\\s+EQUAL\\s+TO\\b|\\bNOT\\s+EQUAL\\b", "!="),
                (r"\\bEQUAL\\s+TO\\b", "=="),
                (r"\\bEQUAL\\b", "=="),
                (r"\\bNOT\\b", "not"),
                (r"\\bAND\\b", "and"),
                (r"\\bOR\\b", "or"),
                (r"\\bSPACES\\b|\\bSPACE\\b", chr(34)+chr(34)),
                (r"\\bZEROS\\b|\\bZERO\\b", "0"),
            ]
            for _pat, _repl in _cobol_ops:
                cond = re.sub(_pat, _repl, cond, flags=re.IGNORECASE)
            cond = cond.replace(" = ", " == ")
            out_lines.append(cur_indent() + "if " + cond + ":")
            if_depth += 1
            changes.append("IF -> if (COBOL operators converted)")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")