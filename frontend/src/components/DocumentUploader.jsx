// components/DocumentUploader.jsx
import React, { useState } from "react";
import './DocumentUploader.css';

export default function DocumentUploader() {
  const [files, setFiles] = useState([]);
  const [msg, setMsg] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadDocs = async () => {
    if (files.length === 0) {
      alert("Please select files to upload");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    files.forEach((f) => formData.append("files", f));
    try {
      const res = await fetch("http://127.0.0.1:5000/api/ingest/documents", {
        method: "POST",
        body: formData
      });
      const json = await res.json();
      setMsg(json.detail || JSON.stringify(json));
    } catch (err) {
      setMsg("Error: " + err);
    }
    setLoading(false);
  };

  return (
    <div className="document-uploader">
      <h2>Upload Documents</h2>
      <input
        type="file"
        multiple
        onChange={(e) => setFiles(Array.from(e.target.files))}
        className="file-input"
      />
      <button className="upload-btn" onClick={uploadDocs} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>
      {msg && <p className="upload-msg">{msg}</p>}
    </div>
  );
}