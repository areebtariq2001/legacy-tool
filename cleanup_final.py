with open(".gitignore", "a", encoding="utf-8") as f:
    f.write("\nnode_modules/\n")
    f.write("ersdellDesktoplegacy-migration-toolbackendmain.py\n")
    f.write("app_code.txt\n")
    f.write("arch_fix_diff.txt\n")
    f.write("indexcheck.txt\n")

print("DONE - .gitignore updated")