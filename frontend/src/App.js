import { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState('analyze');
  const [language, setLanguage] = useState('python');
  const API = 'https://legacy-migration-tool-1.onrender.com';

  const handleSubmit = async () => {
    if (!file) return alert('Please select a file first!');
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    let endpoint = mode === 'analyze' ? '/analyze' : '/migrate';
    if (language === 'java') {
      endpoint = mode === 'analyze' ? '/analyze-java' : '/migrate-java';
    }
    const res = await fetch(API + endpoint, { method: 'POST', body: formData });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  const handleDownload = async () => {
    if (!file) return alert('Please select a file first!');
    const formData = new FormData();
    formData.append('file', file);
    const endpoint = language === 'java' ? '/migrate-java' : '/download';
    const res = await fetch(API + endpoint, { method: 'POST', body: formData });
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = file.name.replace(language === 'java' ? '.java' : '.py', '_migrated' + (language === 'java' ? '.java' : '.py'));
    a.click();
  };

  return (
    <div style={{minHeight:'100vh',background:'#0f172a',color:'white',padding:'40px',fontFamily:'Arial'}}>
      <h1 style={{color:'#38bdf8',textAlign:'center'}}>Legacy Code Migration Tool</h1>
      <p style={{textAlign:'center',color:'#94a3b8'}}>Analyze and migrate your legacy code</p>
      <div style={{maxWidth:'600px',margin:'40px auto',background:'#1e293b',padding:'30px',borderRadius:'12px'}}>
        <div style={{marginBottom:'20px',display:'flex',gap:'10px'}}>
          <button onClick={()=>setLanguage('python')} style={{flex:1,padding:'10px',borderRadius:'8px',border:'none',background:language==='python'?'#7c3aed':'#334155',color:'white',cursor:'pointer'}}>Python
            