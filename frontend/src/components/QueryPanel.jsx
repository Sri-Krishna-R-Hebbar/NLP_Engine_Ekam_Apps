// components/QueryPanel.jsx
import React, { useState } from "react";
import './QueryPanel.css';

export default function QueryPanel({ connectionString, setResults, setShowResults }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const runQuery = async () => {
    if (!connectionString) {
      alert("Please connect to the database first");
      return;
    }
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:5000/api/query/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, connection_string: connectionString })
      });
      const json = await res.json();
      console.log("Query result:", json);
      if (json.status === "success") {
        setResults(json.data);
        setShowResults(true);
      } else {
        alert("Error: " + json.message || JSON.stringify(json));
      }
    } catch (err) {
      console.error("Query error:", err);
      alert("Error: " + err);
    }
    setLoading(false);
  };

  return (
    <div className="query-panel">
      <h2>Run Query</h2>
      <textarea
        className="query-input"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter SQL or natural query"
      />
      <button className="execute-btn" onClick={runQuery} disabled={loading}>
        {loading ? "Executing..." : "Execute"}
      </button>
    </div>
  );
}