# StarBuild - AI-Powered Legacy Code Migration Tool

Transform your legacy code to modern standards instantly. StarBuild analyzes, migrates, and explains legacy code across Python, Java, PHP, and COBOL using AI.

**Live Demo:** https://areebtariq2001.github.io/legacy-migration-tool

**API:** https://legacy-migration-tool-1.onrender.com

---

## Features

- **Multi-Language Support** - Python, Java, PHP, and COBOL
- **Analyze** - Detect legacy patterns and deprecated functions
- **Migrate** - Automatically convert code to modern standards
- **AI Suggest** - Get intelligent improvement suggestions (powered by Groq)
- **Explain Mode** - Understand legacy code with AI explanations
- **Test Generator** - Auto-generate unit tests
- **Diff Viewer** - Side-by-side comparison of original vs migrated code
- **Batch Processing** - Migrate multiple files at once
- **ZIP Download** - Download all migrated files together
- **PDF Reports** - Generate professional migration reports
- **Usage Dashboard** - Track all migrations with audit logs
- **Dark/Light Mode** - Comfortable viewing in any environment
- **REST API** - Integrate into your CI/CD pipeline
- **VS Code Extension** - Migrate code directly from your editor

---

## Tech Stack

**Frontend:**
- React
- react-diff-viewer-continued (diff viewer)
- jsPDF (PDF reports)
- JSZip (ZIP downloads)
- Deployed on GitHub Pages

**Backend:**
- FastAPI (Python)
- Groq AI (llama-3.1-8b-instant)
- Deployed on Render

---

## Supported Migrations

### Python (2 to 3)
- `xrange()` to `range()`
- `raw_input()` to `input()`
- `print` statement to `print()`
- `unicode()` to `str()`

### Java
- `StringBuffer` to `StringBuilder`
- `new Integer()` to `Integer.valueOf()`
- Old-style loops detection
- Vector/Hashtable recommendations

### PHP
- `mysql_*` to `mysqli_*`
- `ereg()` to `preg_match()`
- `split()` to `explode()`
- PHP4-style properties to modern syntax

### COBOL
- DISPLAY to print()
- DIVISION structure conversion
- PERFORM and GOTO detection

---

## API Usage

### Migrate a file (cURL)
```bash
curl -X POST \
  https://legacy-migration-tool-1.onrender.com/migrate \
  -F "file=@myscript.py"
```

### Python
```python
import requests

url = "https://legacy-migration-tool-1.onrender.com/migrate"
files = {"file": open("myscript.py", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Endpoints
| Endpoint | Description |
|----------|-------------|
| POST /analyze | Analyze Python code |
| POST /migrate | Migrate Python 2 to 3 |
| POST /analyze-java, /migrate-java | Java analysis and migration |
| POST /analyze-php, /migrate-php | PHP analysis and migration |
| POST /analyze-cobol, /migrate-cobol | COBOL analysis and migration |
| POST /ai-suggest | AI improvement suggestions |
| POST /explain | AI code explanation |
| POST /generate-tests | Auto-generate unit tests |
| GET /stats | Usage statistics |

---

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

---

## Project Structure
---

## Environment Variables

Backend requires:
- `GROQ_API_KEY` - For AI features (get free key at console.groq.com)

---

## License

MIT License - feel free to use and modify.

---

## Author

Built by Areeb Tariq

2026 StarBuild