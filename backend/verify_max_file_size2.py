import main
result = main.safe_read_file(b"x" * (main.MAX_FILE_SIZE + 1000), "test.py")
print("MAX_FILE_SIZE value:", main.MAX_FILE_SIZE)
print("Oversized file result:", result)