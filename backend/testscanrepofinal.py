import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

# Mock auth for migration-roadmap test
main._check_user_auth = lambda request: "test@example.com"

with open("testscanrepofinal_result.txt", "w", encoding="utf-8") as out:
    r1 = client.post("/scan-repo", json={"repo_url": "https://github.com/octocat/Hello-World"})
    out.write("/scan-repo -> status: " + str(r1.status_code) + " body(first 200): " + r1.text[:200] + chr(10) + chr(10))

    r2 = client.post("/migration-roadmap", json={"repo_url": "https://github.com/octocat/Hello-World"})
    out.write("/migration-roadmap -> status: " + str(r2.status_code) + " body(first 200): " + r2.text[:200])
print("TESTSCANREPOFINAL-DONE")