import main
from fastapi.testclient import TestClient

client = TestClient(main.app)
test_code = b"def hello():\n    print('hello world')\n"

with open("testthreadpool56_result.txt", "w", encoding="utf-8") as out:
    for endpoint in ["/generate-docs", "/ai-consistency-check"]:
        files = {"file": ("test.py", test_code, "text/plain")}
        r = client.post(endpoint, files=files)
        out.write(endpoint + " -> status: " + str(r.status_code) + " body(first 150): " + r.text[:150] + chr(10) + chr(10))
print("TESTTHREADPOOL56-DONE")