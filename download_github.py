import requests
import os
import io
import zipfile

os.makedirs("test_files", exist_ok=True)

# Chhote reliable repos (jaldi download honge)
# Dono branch try karenge: main aur master
repos = [
    "https://github.com/PythonCharmers/python-future/archive/refs/heads/master.zip",
    "https://github.com/faif/python-patterns/archive/refs/heads/master.zip",
]

downloaded = 0

for repo_url in repos:
    print(f"Downloading: {repo_url}")
    try:
        resp = requests.get(repo_url, timeout=60, stream=False)
        if resp.status_code != 200:
            print(f"  Failed: status {resp.status_code}, trying next...")
            continue
        z = zipfile.ZipFile(io.BytesIO(resp.content))
        py_files = [n for n in z.namelist() if n.endswith(".py")]
        print(f"  Found {len(py_files)} Python files")
        for name in py_files[:25]:
            try:
                code = z.read(name).decode("utf-8", errors="ignore")
                if len(code.strip()) < 10:
                    continue
                safe_name = "gh_" + os.path.basename(name)
                with open(os.path.join("test_files", safe_name), "w", encoding="utf-8") as f:
                    f.write(code)
                downloaded += 1
            except Exception as e:
                pass
        if downloaded > 0:
            break  # ek repo mil gaya to bas
    except Exception as e:
        print(f"  Error: {e}, trying next...")

print(f"\nTotal downloaded: {downloaded} Python files")