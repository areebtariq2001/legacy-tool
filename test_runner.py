import os
import requests
import csv

# Tumhara backend URL
API = "https://legacy-migration-tool-1.onrender.com"

# Jis folder mein test files hain
TEST_FOLDER = "test_files"

# Results yahan save honge
OUTPUT_CSV = "test_results.csv"

def test_all_files():
    results = []
    files = [f for f in os.listdir(TEST_FOLDER) if f.endswith(".py")]

    if not files:
        print("test_files folder mein koi .py file nahi mili!")
        return

    print(f"Total {len(files)} files mil gayi. Testing shuru...\n")

    for i, filename in enumerate(files):
        filepath = os.path.join(TEST_FOLDER, filename)
        try:
            with open(filepath, "rb") as f:
                response = requests.post(
                    API + "/ai-migrate",
                    files={"file": (filename, f)},
                    timeout=120
                )
            data = response.json()
            score = data.get("confidence_score", "N/A")
            level = data.get("confidence_level", "N/A")
            reason = data.get("confidence_reason", "")
            print(f"[{i+1}/{len(files)}] {filename} -> {score}% ({level})")
            results.append({
                "filename": filename,
                "confidence_score": score,
                "confidence_level": level,
                "reason": reason
            })
        except Exception as e:
            print(f"[{i+1}/{len(files)}] {filename} -> ERROR: {e}")
            results.append({
                "filename": filename,
                "confidence_score": "ERROR",
                "confidence_level": "failed",
                "reason": str(e)
            })

    # Results CSV mein likho
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "confidence_score", "confidence_level", "reason"])
        writer.writeheader()
        writer.writerows(results)

    # Summary
    scores = [r["confidence_score"] for r in results if isinstance(r["confidence_score"], int)]
    high = len([s for s in scores if s >= 90])
    med = len([s for s in scores if 60 <= s < 90])
    low = len([s for s in scores if s < 60])
    print("\n===== SUMMARY =====")
    print(f"Total files tested: {len(results)}")
    print(f"High confidence (90+): {high}")
    print(f"Need review (60-89): {med}")
    print(f"Low confidence (<60): {low}")
    if scores:
        print(f"Average score: {round(sum(scores)/len(scores))}%")
    print(f"\nResults saved in: {OUTPUT_CSV}")

if __name__ == "__main__":
    test_all_files()