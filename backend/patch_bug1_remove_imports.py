with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = "    import re as _seqre\n"
new1 = ""
old2 = "        import re as _mre\n"
new2 = ""

count1 = content.count(old1)
count2 = content.count(old2)
print("Import _seqre occurrences:", count1)
print("Import _mre occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
if count2 == 1:
    content = content.replace(old2, new2, 1)

content = content.replace("_seqre.", "re.")
content = content.replace("_mre.", "re.")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("PATCHED SUCCESSFULLY")