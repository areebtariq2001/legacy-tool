import main

test_code = '''import sun.misc.Unsafe;
public class Test {
    Date d = new Date();
    void hash() { MessageDigest.getInstance("MD5"); }
    void thread() { Thread.stop(); }
    protected void finalize() { }
}'''

result = main.analyze_java(test_code)
print("Issues found:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)