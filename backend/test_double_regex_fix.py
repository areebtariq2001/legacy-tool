import main

php_result = main.migrate_php('<?php\n$conn = mysql_connect("h", "u", "p");\n?>')
print("PHP still working:", "mysql_connect" in str(php_result["changes"]))

java_result = main.migrate_java('import javax.servlet.http.HttpServlet;')
print("Java still working:", "jakarta" in java_result["migrated_code"])