with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
endpoints = ['"/analyze-php"', '"/migrate-php"', '"/analyze-java"', '"/migrate-java"', '"/analyze-cobol"', '"/migrate-cobol"']
for i, line in enumerate(lines):
    for ep in endpoints:
        if ep in line:
            output_lines.append("=== " + ep + " AT LINE " + str(i + 1) + " ===\n")
            for j in range(i, min(i + 7, len(lines))):
                output_lines.append(str(j + 1) + ": " + lines[j])
            output_lines.append("\n")

with open("all_endpoints_detail_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")