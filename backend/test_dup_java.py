import main

code = """public class Test {
    public void methodOne() {
        System.out.println("Processing transaction data now");
    }
    public void methodTwo() {
        System.out.println("Processing transaction data now");
    }
}"""

r = main.detect_code_smells(code, "Test.java")
print(r.get("smell_summary"))
print(r.get("code_smells"))