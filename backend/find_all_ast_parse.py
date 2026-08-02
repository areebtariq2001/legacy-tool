with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "ast.parse(" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("all_ast_parse_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE - found", len(output_lines), "occurrences")