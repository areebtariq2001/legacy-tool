with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    java_checks = [
        (r"\\bStringBuffer\\b", "StringBuffer found - use StringBuilder"),
        (r"\\bnew\\s+Integer\\s*\\(", "new Integer() found - use Integer.valueOf()"),
        (r"\\bnew\\s+Boolean\\s*\\(", "new Boolean() found - use Boolean.valueOf()"),
        (r"\\bnew\\s+Double\\s*\\(", "new Double() found - use Double.valueOf()"),
        (r"\\bVector\\b", "Vector found - use ArrayList"),
        (r"\\bHashtable\\b", "Hashtable found - use HashMap"),
        (r"\\bEnumeration\\b", "Enumeration found - use Iterator"),
        (r"\\bSystem\\.out\\.println\\b", "System.out.println - consider a logging framework"),
    ]'''

new = '''    java_checks = [
        (r"\\bStringBuffer\\b", "StringBuffer found - use StringBuilder"),
        (r"\\bnew\\s+Integer\\s*\\(", "new Integer() found - use Integer.valueOf()"),
        (r"\\bnew\\s+Boolean\\s*\\(", "new Boolean() found - use Boolean.valueOf()"),
        (r"\\bnew\\s+Double\\s*\\(", "new Double() found - use Double.valueOf()"),
        (r"\\bVector\\b", "Vector found - use ArrayList"),
        (r"\\bHashtable\\b", "Hashtable found - use HashMap"),
        (r"\\bEnumeration\\b", "Enumeration found - use Iterator"),
        (r"\\bSystem\\.out\\.println\\b", "System.out.println - consider a logging framework"),
        (r"MessageDigest\\.getInstance\\s*\\(\\s*[\\x22\\x27]MD5[\\x22\\x27]", "MD5 hashing found - insecure, use SHA-256 or a password-hashing function"),
        (r"MessageDigest\\.getInstance\\s*\\(\\s*[\\x22\\x27]SHA-1[\\x22\\x27]", "SHA-1 hashing found - insecure, use SHA-256"),
        (r"Runtime\\.getRuntime\\(\\)\\.exec\\s*\\(", "Runtime.exec() found - potential command injection risk if input is not sanitized"),
        (r"createStatement\\s*\\(\\s*\\)", "Raw Statement (createStatement) found - use PreparedStatement to prevent SQL injection"),
        (r"\\bnew\\s+Date\\s*\\(\\s*\\)", "new Date() found - consider java.time.LocalDate/LocalDateTime for new code"),
        (r"Calendar\\.getInstance\\b", "Calendar.getInstance() found - consider java.time.LocalDateTime for new code"),
        (r"Thread\\.stop\\b", "Thread.stop() found - deprecated and unsafe, can leave objects in an inconsistent state"),
        (r"import\\s+sun\\.", "import from sun.* package found - these are internal JDK APIs, not part of the public API, and may break across JDK versions"),
        (r"\\bfinalize\\s*\\(\\s*\\)\\s*\\{", "finalize() method found - deprecated since Java 9, removed in Java 18+"),
    ]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")