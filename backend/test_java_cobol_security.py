import main

java_test = '''public class Test {
    String password = "SuperSecret123";
    public void getUser(String id) {
        String sql = "SELECT * FROM users WHERE id = " + id;
    }
}'''
result_java = main.analyze_java(java_test)
print("Java issues:", result_java["issues"])

cobol_test = '''       01 WS-PASSWORD PIC X(20) VALUE "MySecretPass".'''
result_cobol = main.analyze_cobol(cobol_test)
print("COBOL issues:", result_cobol["issues"])