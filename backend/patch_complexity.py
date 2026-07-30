with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = 265
end_idx = 279

print("Line at start (266):", repr(lines[265]))
print("Line at end (279):", repr(lines[278]))

new_block = []
new_block.append("def calculate_complexity(source):\n")
new_block.append('    keywords = ["if ", "elif ", "for ", "while ", "except", " and ", " or ", "case "]\n')
new_block.append("    raw_score = 1\n")
new_block.append("    for kw in keywords:\n")
new_block.append("        raw_score += source.count(kw)\n")
new_block.append('    func_patterns = [r"\\bdef\\s+\\w+\\s*\\(", r"\\bfunction\\s+\\w+\\s*\\(", r"(?:public|private|protected)\\s+(?:static\\s+)?[\\w<>\\[\\]]+\\s+\\w+\\s*\\("]\n')
new_block.append("    func_count = 0\n")
new_block.append("    for fp in func_patterns:\n")
new_block.append("        func_count += len(re.findall(fp, source))\n")
new_block.append("    func_count = max(1, func_count)\n")
new_block.append("    score = round(raw_score / func_count, 1) if func_count > 1 else raw_score\n")
new_block.append("    if score <= 5:\n")
new_block.append('        level = "Low complexity"\n')
new_block.append("    elif score <= 10:\n")
new_block.append('        level = "Moderate complexity"\n')
new_block.append("    elif score <= 20:\n")
new_block.append('        level = "High complexity"\n')
new_block.append("    else:\n")
new_block.append('        level = "Very high complexity"\n')
new_block.append('    return {"complexity_score": score, "complexity_level": level, "raw_keyword_count": raw_score, "estimated_functions": func_count}\n')
new_block.append("\n")

lines[start_idx:end_idx] = new_block

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("PATCHED SUCCESSFULLY")