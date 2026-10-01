import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

with open("testthreadpool9to11_result.txt", "w", encoding="utf-8") as out:
    r1 = client.post("/auth/login", json={"email": "nonexistent@test.com", "password": "wrongpass"})
    out.write("/auth/login -> status: " + str(r1.status_code) + " body: " + r1.text[:150] + chr(10) + chr(10))

    r2 = client.post("/auth/register", json={"email": "newtest_threadpool@test.com", "password": "SecurePass123!"})
    out.write("/auth/register -> status: " + str(r2.status_code) + " body: " + r2.text[:150] + chr(10) + chr(10))

    r3 = client.post("/save-approval", json={"filename": "test.py", "decision": "Approved", "reviewer_notes": "ok", "action_type": "migration"})
    out.write("/save-approval (no-auth) -> status: " + str(r3.status_code) + " body: " + r3.text[:150])
print("TESTTHREADPOOL9TO11-DONE")