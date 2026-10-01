import os
with open("checkdburl_result.txt", "w", encoding="utf-8") as out:
    db_url = os.environ.get("DATABASE_URL", "")
    out.write("Genuinely-DATABASE_URL-is-set: " + str(bool(db_url)) + chr(10))
    if db_url:
        out.write("Genuinely-DATABASE_URL-length: " + str(len(db_url)))
print("CHECKDBURL-DONE")