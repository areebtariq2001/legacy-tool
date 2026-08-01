import main

test_code = '''public class Test {
    public void hash() {
        MessageDigest md = MessageDigest.getInstance("MD5");
    }
    public void run(String cmd) {
        Runtime.getRuntime().exec(cmd);
    }
    public void query() {
        Statement s = conn.createStatement();
    }
}'''

result = main.analyze_java(test_code)
print("Issues found:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)