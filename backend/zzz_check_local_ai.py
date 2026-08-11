import main
import asyncio

result = asyncio.run(main.local_ai_status_endpoint())
with open("zzz_local_ai_result.txt", "w") as f:
    f.write(str(result))
print("DONE")