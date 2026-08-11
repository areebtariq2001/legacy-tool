import main

with open("zzz_cmd_search.txt", "w") as f:
    for name in dir(main):
        if 'command' in name.lower() and 'inject' in name.lower():
            f.write(name + "\n")
        if 'scan_sensitive' in name.lower():
            f.write(name + "\n")

print("DONE")