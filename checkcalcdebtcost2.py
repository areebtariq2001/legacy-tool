main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def calculate_tech_debt_cost")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

ridx = body.rfind("return {")

with open("checkcalcdebtcost2_result.txt", "w", encoding="utf-8") as out:
    out.write(body[ridx:ridx+700])
print("CHECKCALCDEBTCOST2-DONE")