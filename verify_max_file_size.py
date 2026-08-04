import main
import inspect

src = inspect.getsource(main.safe_read_file)
with open("max_file_size_output.txt", "w", encoding="utf-8") as out:
    out.write("MAX_FILE_SIZE value: " + str(main.MAX_FILE_SIZE) + "\n\n")
    out.write("safe_read_file source:\n")
    out.write(src)

print("DONE")