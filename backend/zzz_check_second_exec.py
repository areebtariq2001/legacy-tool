with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("zzz_second_exec_out.txt", "w") as out:
    idx = content.find("_sp2")
    if idx != -1:
        out.write(content[max(0,idx-500):idx+800])
    else:
        out.write("Not found")

print("DONE")