import main

java_code = "import java.util.Vector;\n\npublic class Test {\n}\n"
result = main.assess_dependency_risk(java_code, "Test.java")

with open("final_debug_test_result.txt", "w", encoding="utf-8") as out:
    out.write("total_findings: " + str(result.get("total_findings")) + chr(10))
    out.write("findings: " + str(result.get("findings")) + chr(10) + chr(10))

    # Check the exact Vector rule tuple structure
    for rule in main.JAVA_RISK_RULES:
        if rule[0] == "Vector":
            out.write("Vector-rule-tuple: " + repr(rule) + chr(10))
            out.write("rule[0]-repr: " + repr(rule[0]) + chr(10))
            out.write("len-of-rule-tuple: " + str(len(rule)) + chr(10))
print("FINAL-DEBUG-TEST-COMPLETED")