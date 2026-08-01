import main

test_code = '''import javax.servlet.http.HttpServlet;
@WebServlet("/api")
public class MyServlet extends HttpServlet {
    Vector<String> items = new Vector<>();
    Integer x = new Integer(5);
    Enumeration<String> e = items.elements();
}'''

result = main.migrate_java(test_code)
print("=== Auto-applied changes ===")
for c in result["changes"]:
    if not c.startswith("REVIEW NEEDED"):
        print(" AUTO:", c)
print()
print("=== Review Needed ===")
for c in result["changes"]:
    if c.startswith("REVIEW NEEDED"):
        print(" REVIEW:", c[:70])
print()
print("Vector genuinely unchanged in code:", "Vector<String>" in result["migrated_code"])
print("Integer.valueOf genuinely applied:", "Integer.valueOf(5)" in result["migrated_code"])