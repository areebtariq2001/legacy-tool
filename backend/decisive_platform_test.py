import main
r1 = main.check_platform_compatibility('path = "C:\\\\data"', "test.py")
r2 = main.calculate_dependency_portability("x=1", "test.py")
with open("decisive_platform_result.txt", "w", encoding="utf-8") as out:
    out.write("PLATFORM-RESULT: " + str(r1) + chr(10) + chr(10))
    out.write("PORTABILITY-RESULT: " + str(r2))
print("DECISIVE-PLATFORM-TEST-COMPLETED")