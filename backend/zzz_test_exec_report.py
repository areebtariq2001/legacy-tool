import main

test_java = '''public class Test {
    public void evaluate_score() {
        System.out.println("test");
    }
}'''

result = main.generate_executive_report(test_java, "Test.java")
print("Java exec_health:", result["exec_health"])
print("Java exec_stats:", result["exec_stats"])
print("Findings:", result["exec_findings"])