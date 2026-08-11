with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

endpoints = ["ai-native-readiness", "predict-risk", "cicd-recommendations", "analyze-db-schema", "map-api-dependencies", "generate-architecture"]

with open("zzz_status_check_out.txt", "w") as out:
    for ep in endpoints:
        idx = content.find('"' + ep + '"')
        chunk = content[idx:idx+700]
        has_jsonresponse = "JSONResponse" in chunk
        out.write(ep + " : JSONResponse-used=" + str(has_jsonresponse) + "\n")

print("DONE")