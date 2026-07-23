import main
code = "def hello():\n    print('hello world')"
r = main.generate_living_documentation(code, "test_living.py")
print(r.get("living_doc_summary"))
print(r.get("living_doc_version"))