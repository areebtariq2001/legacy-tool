import main

test_code = '''import java.util.*;
public class UserService {
    public UserService() { }
    public List<User> getUsers() { return null; }
    public Map<String, Integer> getCounts() { return null; }
}'''

result = main.analyze_java(test_code)
print("Methods:", result["methods"])
print("Total methods:", result.get("total_methods"))
print("Methods truncated:", result.get("methods_truncated"))
print("Issues:", result["issues"])