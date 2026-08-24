lines = []
lines.append('def generate_compatibility_matrix(source, filename):')
lines.append('    if len(source.encode("utf-8", errors="ignore")) > MAX_FILE_SIZE:')
lines.append('        return {"matrix_generated": False, "targets": [], "matrix_summary": "File too large."}')
lines.append('    is_python = filename.lower().endswith(".py")')
lines.append('    is_java = filename.lower().endswith(".java")')
lines.append('    if not (is_python or is_java):')
lines.append('        return {"matrix_generated": False, "targets": [], "matrix_summary": "Only Python and Java supported."}')
lines.append('    targets = []')

with open("compat_lines_1.txt", "w", encoding="utf-8") as f:
    f.write(chr(10).join(lines))
print("PART-1-SAVED")