import main
code = "MAIN-LOGIC.\nEXEC CICS RETURN END-EXEC."
r = main.analyze_vendor_lockin(code, "test.cbl")
print(r.get("lockin_summary"))