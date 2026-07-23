import main
code = "MAIN-LOGIC.\nDISPLAY 1."
r = main.analyze_vendor_lockin(code, "test.cbl")
print(r.get("lockin_summary"))