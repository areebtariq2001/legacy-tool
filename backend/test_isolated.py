import main
code = "import javax.servlet.http.HttpServlet;"
r = main.migrate_java(code)
print(repr(r.get("migrated_code")))