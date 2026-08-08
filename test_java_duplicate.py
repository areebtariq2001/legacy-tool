import main

test_java = '''import java.security.MessageDigest;
public class Test {
    public void getUser(String id) {
        String query = "SELECT * FROM users WHERE id = " + id;
        MessageDigest md = MessageDigest.getInstance("MD5");
    }
}'''

result = main.analyze_java(test_java)
for issue in result["issues"]:
    print("-", issue)