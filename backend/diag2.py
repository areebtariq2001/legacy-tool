main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("diag2_result.txt", "w", encoding="utf-8") as out:
    out.write("'CBS' count: " + str(content.count("CBS")) + chr(10))
    out.write("'Core-Banking' count: " + str(content.count("Core-Banking")) + chr(10))
    out.write("'potential CBS' count: " + str(content.count("potential CBS")) + chr(10))
    out.write("'scan_cbs_integration_points' count: " + str(content.count("scan_cbs_integration_points")) + chr(10))
    idx = content.find("scan_cbs_integration_points")
    idx2 = content.find("scan_cbs_integration_points", idx+1)
    if idx2 != -1:
        out.write("SECOND occurrence context: " + content[max(0,idx2-30):idx2+400])
print("DIAG2-DONE")