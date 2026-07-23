import re
cond = "WS-IS-FLAGGED = " + chr(34) + "Y" + chr(34)
result = re.sub(r"[\x22\x27][^\x22\x27]*[\x22\x27]|[A-Za-z][\w-]*", lambda m: m.group(0) if (m.group(0)[0] in chr(34)+chr(39)) else m.group(0).replace("-", "_"), cond)
print(result)
