gitignore_content = """*.txt
fix_*.py
get_*.py
check_*.py
test_*.py
add_*.py
view_*.py
debug_*.py
"""

with open("backend/.gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)

print("DONE - .gitignore created")