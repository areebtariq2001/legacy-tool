import main

java_code = "import org.apache.log4j.Logger;\npublic class Test { void x() { ObjectInputStream ois = null; } }"
result1 = main.assess_dependency_risk(java_code, "Test.java")
print("Java test:", result1["overall_risk"], "- findings:", len(result1["findings"]))
for f in result1["findings"]:
    print(" -", f["dependency"], f["risk_level"])

php_code = "<?php\n$pw = md5($password);\neval($x);\n?>"
result2 = main.assess_dependency_risk(php_code, "test.php")
print("PHP test:", result2["overall_risk"], "- findings:", len(result2["findings"]))
for f in result2["findings"]:
    print(" -", f["dependency"], f["risk_level"])

cobol_result = main.assess_dependency_risk("SOME COBOL", "test.cbl")
print("COBOL test:", cobol_result["overall_risk"])