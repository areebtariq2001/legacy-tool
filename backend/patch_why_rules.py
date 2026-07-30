with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Add language-specific WHY_RULES lists right after WHY_RULES definition
old1 = '''    ("except", "Python 3 requires the 'except Exception as e' syntax. The old comma form 'except Exception, e' was removed."),
]

def get_why_explanations(original_source):
    explanations = []
    if "print " in original_source and not "print(" in original_source.split("print ")[0][-5:]:
        explanations.append({"change": "print statement -> print()", "why": "In Python 3, print is a function, not a statement. It must be called with parentheses, e.g. print(x)."})
    for keyword, reason in WHY_RULES:
        if keyword in original_source:
            explanations.append({"change": keyword, "why": reason})
    return explanations'''

new1 = '''    ("except", "Python 3 requires the 'except Exception as e' syntax. The old comma form 'except Exception, e' was removed."),
]

JAVA_WHY_RULES = [
    ("Vector", "Vector is a legacy synchronized collection from Java 1.0. ArrayList is preferred unless thread-safety is specifically required."),
    ("Hashtable", "Hashtable is a legacy synchronized map. HashMap (or ConcurrentHashMap for thread-safety) is the modern equivalent."),
    ("StringBuffer", "StringBuffer is synchronized and slower than StringBuilder. Use StringBuilder unless multiple threads mutate the same instance."),
    ("System.out.println", "Direct System.out.println calls are hard to control in production. A logging framework (SLF4J, Log4j) allows log levels and centralized output control."),
]

PHP_WHY_RULES = [
    ("mysql_", "The mysql_* extension was removed in PHP 7. mysqli_* or PDO should be used instead, and they support prepared statements which also prevent SQL injection."),
    ("each(", "each() was removed in PHP 8. Use a foreach loop instead, which is both simpler and faster."),
    ("create_function", "create_function() was removed in PHP 8 due to security risks (it used eval internally). Use an anonymous function (closure) instead."),
]

COBOL_WHY_RULES = [
    ("GO TO", "GO TO creates unstructured control flow that is difficult to trace and migrate. Modern structured constructs (IF/PERFORM) are safer to convert automatically."),
    ("REDEFINES", "REDEFINES reinterprets the same memory as a different data type, which has no direct equivalent in modern languages and requires manual translation of the intended logic."),
    ("ALTER", "The ALTER statement dynamically changes a GO TO target at runtime. This pattern is deprecated even in COBOL itself and needs manual review to convert safely."),
]

def get_why_explanations(original_source, language="python"):
    explanations = []
    if language == "python":
        if "print " in original_source and not "print(" in original_source.split("print ")[0][-5:]:
            explanations.append({"change": "print statement -> print()", "why": "In Python 3, print is a function, not a statement. It must be called with parentheses, e.g. print(x)."})
        for keyword, reason in WHY_RULES:
            if keyword in original_source:
                explanations.append({"change": keyword, "why": reason})
    elif language == "java":
        for keyword, reason in JAVA_WHY_RULES:
            if keyword in original_source:
                explanations.append({"change": keyword, "why": reason})
    elif language == "php":
        for keyword, reason in PHP_WHY_RULES:
            if keyword in original_source:
                explanations.append({"change": keyword, "why": reason})
    elif language == "cobol":
        for keyword, reason in COBOL_WHY_RULES:
            if keyword.upper() in original_source.upper():