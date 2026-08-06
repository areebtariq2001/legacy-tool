import main

test_code = '''def aml_check():
    print "Running AML validation"          # py2 print statement (removed in py3)
    return True'''

result = main.migrate_code(test_code)
print(result["migrated_code"])
print()
print("=== Genuinely-valid-Python check ===")
try:
    compile(result["migrated_code"], "<test>", "exec")
    print("VALID PYTHON")
except SyntaxError as e:
    print("SYNTAX ERROR:", e)