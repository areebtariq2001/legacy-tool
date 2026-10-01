main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('_endpoint_identifier =')
idx_end = content.find("\n\n", idx)
if idx_end == -1 or idx_end - idx > 1500:
    idx_end = idx + 1000

with open("checkfullratelimit_result.txt", "w", encoding="utf-8") as out:
    out.write(content[max(0,idx-1200):idx_end])
print("CHECKFULLRATELIMIT-DONE")