with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def migrate_java(source):
    changes = []
    migrated = source
    rules = [
        (r'\\bnew\\s+Integer\\(', 'Integer.valueOf(', "new Integer() -> Integer.valueOf()"),
        (r'\\bnew\\s+Boolean\\(', 'Boolean.valueOf(', "new Boolean() -> Boolean.valueOf()"),
        (r'\\bnew\\s+Double\\(', 'Double.valueOf(', "new Double() -> Double.valueOf()"),
        (r'\\bnew\\s+Long\\(', 'Long.valueOf(', "new Long() -> Long.valueOf()"),
        (r'\\bStringBuffer\\b', 'StringBuilder', "StringBuffer -> StringBuilder"),
        (r'\\bVector\\b', 'ArrayList', "Vector -> ArrayList"),
        (r'\\bimport javax\\.servlet\\.', 'import jakarta.servlet.', "javax.servlet -> jakarta.servlet (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.persistence\\.', 'import jakarta.persistence.', "javax.persistence -> jakarta.persistence (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.annotation\\.', 'import jakarta.annotation.', "javax.annotation -> jakarta.annotation (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.ejb\\.', 'import jakarta.ejb.', "javax.ejb -> jakarta.ejb (Jakarta EE 9+ namespace)"),
        (r'@WebServlet\\b', '@RestController', "@WebServlet -> @RestController (Spring Boot mapping, review routing)"),
        (r'@Stateless\\b', '@Service', "@Stateless (EJB) -> @Service (Spring), review transaction boundaries"),
        (r'@Stateful\\b', '@Service', "@Stateful (EJB) -> @Service (Spring), review session-scoped state handling"),
        (r'@EJB\\b', '@Autowired', "@EJB -> @Autowired (Spring DI mapping)"),
        (r'@Resource\\b', '@Autowired', "@Resource (JNDI) -> @Autowired (Spring DI mapping)"),
        (r'\\bimport javax\\.ejb\\.Stateless;', 'import org.springframework.stereotype.Service;', "javax.ejb.Stateless import -> Spring Service import"),
        (r'\\bimport javax\\.annotation\\.Resource;', 'import org.springframework.beans.factory.annotation.Autowired;', "javax.annotation.Resource import -> Spring Autowired import"),
        (r'\\.elementAt\\(', '.get(', "Vector.elementAt() -> ArrayList.get()"),
        (r'\\.addElement\\(', '.add(', "Vector.addElement() -> ArrayList.add()"),
        (r'\\.removeElement\\(', '.remove(', "Vector.removeElement() -> ArrayList.remove()"),
        (r'\\bHashtable\\b', 'HashMap', "Hashtable -> HashMap"),
        (r'\\bEnumeration\\b', 'Iterator', "Enumeration -> Iterator"),
    ]
    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)
    return {"migrated_code": migrated, "changes": changes}'''

new = '''def migrate_java(source):
    changes = []
    migrated = source
    rules = [
        (r'\\bnew\\s+Integer\\(', 'Integer.valueOf(', "new Integer() -> Integer.valueOf()"),
        (r'\\bnew\\s+Boolean\\(', 'Boolean.valueOf(', "new Boolean() -> Boolean.valueOf()"),
        (r'\\bnew\\s+Double\\(', 'Double.valueOf(', "new Double() -> Double.valueOf()"),
        (r'\\bnew\\s+Long\\(', 'Long.valueOf(', "new Long() -> Long.valueOf()"),
        (r'\\bimport javax\\.servlet\\.', 'import jakarta.servlet.', "javax.servlet -> jakarta.servlet (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.persistence\\.', 'import jakarta.persistence.', "javax.persistence -> jakarta.persistence (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.annotation\\.', 'import jakarta.annotation.', "javax.annotation -> jakarta.annotation (Jakarta EE 9+ namespace)"),
        (r'\\bimport javax\\.ejb\\.', 'import jakarta.ejb.', "javax.ejb -> jakarta.ejb (Jakarta EE 9+ namespace)"),
    ]
    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)
    review_rules = [
        (r'\\bStringBuffer\\b', "StringBuffer found - StringBuilder is the modern replacement, but StringBuffer is thread-safe and StringBuilder is NOT. Only switch if this code is genuinely single-threaded."),
        (r'\\bVector\\b', "Vector found - ArrayList is the modern replacement, but Vector is synchronized (thread-safe) and ArrayList is NOT. Review for concurrent access before switching, or use Collections.synchronizedList()."),
        (r'\\bHashtable\\b', "Hashtable found - HashMap is the modern replacement, but Hashtable is synchronized (thread-safe) and HashMap is NOT. Review for concurrent access before switching, or use ConcurrentHashMap."),
        (r'\\bEnumeration\\b', "Enumeration found - Iterator is the modern replacement, but the method calls differ (hasMoreElements()/nextElement() vs hasNext()/next()). Renaming the type alone will not compile - all method calls must also be updated."),
        (r'@WebServlet\\b', "@WebServlet found - this is a Servlet-API class using doGet()/doPost() with HttpServletRequest/Response. Converting to Spring's @RestController requires rewriting the method signatures entirely (e.g. @GetMapping methods with different parameters and return types), not just swapping the annotation."),
        (r'@Stateless\\b', "@Stateless (EJB) found - converting to Spring's @Service requires reviewing transaction-boundary annotations (@Transactional) and dependency-injection style, since EJB and Spring have different lifecycle and injection semantics."),
        (r'@Stateful\\b', "@Stateful (EJB) found - converting to Spring requires explicit session-scoped bean configuration (@SessionScope or similar), since Spring's default @Service is not automatically per-session like a Stateful EJB."),
        (r'@EJB\\b', "@EJB found - @Autowired (Spring) is usually a safe replacement for simple field injection, but review if this @EJB reference relies on JNDI lookup semantics that differ from Spring's dependency injection."),
        (r'@Resource\\b', "@Resource found - this can be either simple field injection OR a JNDI lookup (e.g. for a DataSource). @Autowired only covers the injection case - JNDI-looked-up resources need explicit Spring bean configuration instead."),
    ]
    for pattern, msg in review_rules:
        if re.search(pattern, migrated):
            changes.append("REVIEW NEEDED: " + msg)
    return {"migrated_code": migrated, "changes": changes}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")