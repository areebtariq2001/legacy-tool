import React, { useState } from 'react';
import ReactDiffViewer from 'react-diff-viewer-continued';

function App() {
  const [files, setFiles] = useState(null);
  const [result, setResult] = useState({});
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState(0); // Kaunsa tab active hai
  
  const API_BASE_URL = "https://legacy-migration-tool-production.up.railway.app";

  const handleFileChange = (e) => setFiles(e.target.files);

  const handleAction = async (endpoint) => {
    if (!files || files.length === 0) return alert("Please select files first!");
    setLoading(true);
    
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    try {
      const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data);
      setActiveTab(0); // Nayi request par pehla tab select karein
    } catch (error) {
      alert("Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", backgroundColor: "#0d1117", color: "#c9d1d9", minHeight: "100vh" }}>
      <h1 style={{ textAlign: "center" }}>Legacy Migration Tool</h1>
      
      <div style={{ textAlign: "center", marginBottom: "30px", padding: "20px", border: "1px solid #30363d" }}>
        <input type="file" multiple onChange={handleFileChange} />
        <button onClick={() => handleAction("migrate")}>Migrate Files</button>
        <button onClick={() => handleAction("ai-suggest")}>AI Suggest</button>
      </div>

      {/* Migration Result - Tabbed UI */}
      {result.migrated_code && (
        <div>
          <h3>AI Analysis/Migration</h3>
          <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
             {/* Yahan hum sirf ek hi result dikha rahe hain, 
                 agar backend har file ka alag object dega to hum tabs map kar sakte hain */}
             <button onClick={() => setActiveTab(0)}>Result View</button>
          </div>
          <ReactDiffViewer 
            oldValue={result.original_code} 
            newValue={result.migrated_code} 
            splitView={true} 
          />
        </div>
      )}

      {/* AI Suggestions (Emoji Removed) */}
      {result.suggestions && (
        <div style={{ marginTop: "30px", padding: "20px", backgroundColor: "#161b22", border: "1px solid #30363d" }}>
          <h3>AI Suggestions</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>{result.suggestions}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
