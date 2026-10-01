import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

test_code = b"def hello():\n    print('hello world')\n"
files = {"file": ("test.py", test_code, "text/plain")}
r = client.post("/ai-migrate", files=files)

with open("testthreadpool1_result.txt", "w", encoding="utf-8") as out:
    out.write("status: " + str(r.status_code) + chr(10))
    out.write("body (first 500 chars): " + r.text[:500])
print("TESTTHREADPOOL1-DONE")