import React from "react";

function Footer({ darkMode }) {
  return (
    <div style={{
      marginTop: "40px",
      paddingTop: "20px",
      paddingBottom: "20px",
      borderTop: darkMode ? "1px solid #1e293b" : "1px solid #e2e8f0",
      textAlign: "center"
    }}>
      <p style={{ color: "#94a3b8", fontSize: "13px", margin: "0 0 6px 0" }}>
        StarBuild — Predictable, AST-verified, audit-ready legacy migration.
      </p>
      <a href="https://github.com/areebtariq2001/legacy-tool"
         target="_blank" rel="noopener noreferrer"
         style={{ color: "#38bdf8", fontSize: "13px", textDecoration: "none" }}>
        View on GitHub
      </a>
    </div>
  );
}

export default Footer;