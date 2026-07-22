import main
code = """01 DB-PASSWORD PIC X(20) VALUE "Cobol1985Pass".
MAIN-LOGIC.
    DISPLAY 1."""
r = main.generate_code_dna(code, "test.cbl")
print(r.get("dna_dimensions"))