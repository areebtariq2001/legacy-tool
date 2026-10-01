import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

r1 = client.post("/auth/logout", headers={"x-session-token": "some-token-value"})
r2 = client.post("/auth/logout")

with open("testlogout_result.txt", "w", encoding="utf-8") as out:
    out.write("Test-1 (with-token): status=" + str(r1.status_code) + " body=" + r1.text + chr(10))
    out.write("Test-2 (no-token): status=" + str(r2.status_code) + " body=" + r2.text)
print("TESTLOGOUT-DONE")