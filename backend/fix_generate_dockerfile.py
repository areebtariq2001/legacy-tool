with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def generate_dockerfile(filename, language):
    lang = (language or "python").lower()
    if lang == "python":
        content = "# Auto-generated Dockerfile for modernized Python code\\nFROM python:3.11-slim\\n\\nWORKDIR /app\\n\\nCOPY requirements.txt .\\nRUN pip install --no-cache-dir -r requirements.txt\\n\\nCOPY . .\\n\\nCMD [\\"python\\", \\"" + filename + "\\"]\\n"
    elif lang == "java":
        content = "# Auto-generated Dockerfile for modernized Java code\\nFROM openjdk:17-slim\\n\\nWORKDIR /app\\n\\nCOPY . .\\n\\nRUN javac *.java\\n\\nCMD [\\"java\\", \\"Main\\"]\\n"
    elif lang == "php":
        content = "# Auto-generated Dockerfile for modernized PHP code\\nFROM php:8.2-apache\\n\\nCOPY . /var/www/html/\\n\\nEXPOSE 80\\n"
    else:
        content = "# Auto-generated Dockerfile\\nFROM ubuntu:22.04\\n\\nWORKDIR /app\\nCOPY . .\\n"
    return {
        "dockerfile": content,
        "dockerfile_note": "This is a standard starter Dockerfile template to containerize the modernized code. Review and adjust dependencies, entry point, and ports for your environment before deploying."
    }'''

new = '''def generate_dockerfile(filename, language):
    lang = re.sub(r"[\\r\\n]", " ", str(language or "python"))[:30].strip().lower()
    safe_filename = re.sub(r"[^\\w.\\-]", "", str(filename or "app.py"))
    if not safe_filename:
        safe_filename = "app.py"
    if lang == "python":
        content = ("# Auto-generated Dockerfile for modernized Python code\\n"
            "FROM python:3.11-slim\\n\\nWORKDIR /app\\n\\nCOPY . .\\n"
            "RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi\\n\\n"
            "CMD [\\"python\\", \\"" + safe_filename + "\\"]\\n")
    elif lang == "java":
        content = ("# Auto-generated Dockerfile for modernized Java code (Maven-based build)\\n"
            "# NOTE: assumes a standard Maven project layout (pom.xml + src/). Adjust if using Gradle.\\n"
            "FROM maven:3.9-eclipse-temurin-17 AS build\\n"
            "WORKDIR /app\\n"
            "COPY pom.xml .\\n"
            "COPY src ./src\\n"
            "RUN mvn -q package -DskipTests\\n\\n"
            "FROM eclipse-temurin:17-jre-alpine\\n"
            "WORKDIR /app\\n"
            "COPY --from=build /app/target/*.jar app.jar\\n"
            "CMD [\\"java\\", \\"-jar\\", \\"app.jar\\"]\\n")
    elif lang == "php":
        content = ("# Auto-generated Dockerfile for modernized PHP code\\n"
            "FROM php:8.2-apache\\n\\nCOPY . /var/www/html/\\n\\nEXPOSE 80\\n")
    elif lang == "cobol":
        cobol_base = re.sub(r"\\.(cbl|cob)$", "", safe_filename, flags=re.IGNORECASE)
        content = ("# Auto-generated Dockerfile for COBOL (GnuCOBOL)\\n"
            "FROM ubuntu:22.04\\n"
            "RUN apt-get update && apt-get install -y gnucobol4 && rm -rf /var/lib/apt/lists/*\\n"
            "WORKDIR /app\\n"
            "COPY . .\\n"
            "RUN cobc -x -o " + cobol_base + " " + safe_filename + "\\n"
            "CMD [\\"./" + cobol_base + "\\"]\\n")
    else:
        content = "# Auto-generated Dockerfile\\nFROM ubuntu:22.04\\n\\nWORKDIR /app\\nCOPY . .\\n"
    return {
        "dockerfile": content,
        "dockerfile_note": "This is a standard starter Dockerfile template to containerize the modernized code. Review and adjust dependencies, entry point, and ports for your environment before deploying. For Java, assumes a Maven layout (pom.xml/src) - adjust if your project uses Gradle or a different structure."
    }'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")