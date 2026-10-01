import main

test_code = '''condition = "active"
person_name = 'Ali'
phone = "0300"
connection = "established"
onSuccess = "callback_name"'''

test_xss = '<div onclick="alert(1)">click</div>'

result_code = main.sanitize_ai_output(test_code)
result_xss = main.sanitize_ai_output(test_xss)

with open("testsanitize_result.txt", "w", encoding="utf-8") as out:
    out.write("=== Code-preservation-test (should be UNCHANGED) ===\n")
    out.write(result_code + chr(10) + chr(10))
    out.write("Genuinely-code-unchanged: " + str(result_code == test_code) + chr(10) + chr(10))
    out.write("=== XSS-sanitization-test (onclick should be REMOVED) ===\n")
    out.write(result_xss + chr(10))
    out.write("Genuinely-onclick-removed: " + str("onclick" not in result_xss))
print("TESTSANITIZE-DONE")