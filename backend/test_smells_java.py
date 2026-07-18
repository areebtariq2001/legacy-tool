import main

code = """public class Test {
    public String process(int a, int b, int c) {
        if (a > 0) {
            if (b > 0) {
                if (c > 0) {
                    return "all positive";
                }
            }
        }
        return "no";
    }
}"""

r = main.detect_code_smells(code, "Test.java")
print(r.get("smell_summary"))
print(r.get("code_smells"))