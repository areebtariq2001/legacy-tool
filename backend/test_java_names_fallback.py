import main

# Simulate javalang failure by using unusual/broken syntax
java_code = '''public class Account {
    private int balance;
    public void deposit(int amount) {
        balance = balance + amount;
    }
}'''

names = main.extract_java_names(java_code)
print("Names extracted:", names)