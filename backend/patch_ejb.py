with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        (r'@WebServlet\\b', '@RestController', "@WebServlet -> @RestController (Spring Boot mapping, review routing)"),'''
new = old + '''
        (r'@Stateless\\b', '@Service', "@Stateless (EJB) -> @Service (Spring), review transaction boundaries"),
        (r'@Stateful\\b', '@Service', "@Stateful (EJB) -> @Service (Spring), review session-scoped state handling"),
        (r'@EJB\\b', '@Autowired', "@EJB -> @Autowired (Spring DI mapping)"),
        (r'@Resource\\b', '@Autowired', "@Resource (JNDI) -> @Autowired (Spring DI mapping)"),
        (r'\\bimport javax\\.ejb\\.Stateless;', 'import org.springframework.stereotype.Service;', "javax.ejb.Stateless import -> Spring Service import"),
        (r'\\bimport javax\\.annotation\\.Resource;', 'import org.springframework.beans.factory.annotation.Autowired;', "javax.annotation.Resource import -> Spring Autowired import"),'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")