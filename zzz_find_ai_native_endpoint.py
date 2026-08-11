import main

for r in main.app.routes:
    if hasattr(r, 'path') and 'ai-native' in r.path.lower():
        print(r.path)