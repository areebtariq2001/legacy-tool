import React, { useState } from 'react';
import ReactDiffViewer from 'react-diff-viewer-continued';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState({});
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleMigrate = async () => {
    if (!file) return alert("Please select a file first!");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("https://legacy-migration-tool-1.onrender.com/migrate", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Migration Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ padding: "20px", color: "white", backgroundColor: "#0d1117", minHeight: "100vh" }}>
      <h1>Legacy Migration Tool</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleMigrate} disabled={loading}>
        {loading ? "Migrating..." : "Migrate Files"}
      </button>

      {result.migrated_code && (
        <div style={{ marginTop: "20px", border: "1px solid #444", borderRadius: "10px", padding: "15px" }}>
          <h3>Side-by-Side Comparison</h3>
          <ReactDiffViewer 
            oldValue={result.original_code} 
            newValue={result.migrated_code} 
            splitView={true} 
            styles={{
              variables: {
                diffViewerBackground: "#0d1117",
                addedBackground: "#1e3a1e",
                removedBackground: "#4a1c1c",
                wordDiffColor: "#fff"
              }
            }}
          />
        </div>
      )}
    </div>
  );
}

export default App;