with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "        (r'\\bVector\\b', 'ArrayList', \"Vector -> ArrayList\"),"
new = old + "\n        (r'\\bimport javax\\.servlet\\.', 'import jakarta.servlet.', \"javax.servlet -> jakarta.servlet (Jakarta EE 9+ namespace)\"),\n        (r'\\bimport javax\\.persistence\\.', 'import jakarta.persistence.', \"javax.persistence -> jakarta.persistence (Jakarta EE 9+ namespace)\"),\n        (r'\\bimport javax\\.annotation\\.', 'import jakarta.annotation.', \"javax.annotation -> jakarta.annotation (Jakarta EE 9+ namespace)\"),\n        (r'\\bimport javax\\.ejb\\.', 'import jakarta.ejb.', \"javax.ejb -> jakarta.ejb (Jakarta EE 9+ namespace)\"),\n        (r'@WebServlet\\b', '@RestController', \"@WebServlet -> @RestController (Spring Boot mapping, review routing)\"),"

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - not exactly 1 occurrence, aborting to be safe")