import main

with open("testissuechecks2_result.txt", "w", encoding="utf-8") as out:
    test_code_fp = "def my_has_key_func(x):\n    return x\n\ndef misapply(x):\n    return x\n\ndef string_reduce(x):\n    return x"
    result_fp = main.analyze_code(test_code_fp)
    issues_fp = result_fp.get("issues", [])
    out.write("Test-1 (false-positive-code, should have NO py2-related issues): " + str(issues_fp) + chr(10))
    out.write("Genuinely-has_key-falsely-triggered: " + str(any("has_key" in str(i) for i in issues_fp)) + " (expect False)" + chr(10) + chr(10))

    test_code_genuine = "class Foo:\n    def check(self, d, k):\n        if d.has_key(k):\n            pass\n\nresult = apply(func, args)\nx = reduce(f, lst)"
    result_genuine = main.analyze_code(test_code_genuine)
    issues_genuine = result_genuine.get("issues", [])
    out.write("Test-2 (genuine-py2-code, should have has_key/apply/reduce issues): " + str(issues_genuine) + chr(10))
print("TESTISSUECHECKS2-DONE")