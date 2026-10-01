main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkdbconn_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("def _get_db_connection")
    idx_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx_end] + chr(10) + chr(10))
    out.write("Genuinely-import-psycopg2-line: " + chr(10))
    for line in content.split(chr(10)):
        if "psycopg2" in line and "import" in line:
            out.write(line + chr(10))
    out.write(chr(10) + "Genuinely-_get_db_connection-call-count: " + str(content.count("_get_db_connection()")))
print("CHECKDBCONN-DONE")