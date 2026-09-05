with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
with open("struct_part1_out.txt", "r", encoding="utf-8") as f:
    part1 = f.read()
with open("struct_part2_out.txt", "r", encoding="utf-8") as f:
    part2 = f.read()

anchor = '@app.post("/hidden-business-logic")'
c = content.count(anchor)
print("Anchor-count:", c)

new_endpoint = part1 + chr(10) + part2 + chr(10) + anchor
if c == 1:
    content = content.replace(anchor, new_endpoint, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("STRUCT-COMBINED-DONE")
else:
    print("FAILED")