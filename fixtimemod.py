main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old1 = "        import time as _time_mod\n        _scan_start_time = _time_mod.time()"
new1 = "        _scan_start_time = time.time()"
results["1_remove_import"] = content.count(old1)
content = content.replace(old1, new1, 1)

old2 = "_time_mod.time() - _scan_start_time"
new2 = "time.time() - _scan_start_time"
results["2_replace_usage"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXTIMEMOD-DONE")