import main

for r in main.app.routes:
    if hasattr(r, 'path') and 'ai-native' in r.path.lower():
        with open("zzz_ai_native_endpoint.txt", "w") as f:
            f.write(r.path)

print("DONE")