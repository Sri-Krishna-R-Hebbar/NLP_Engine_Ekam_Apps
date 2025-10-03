import React, { useState } from "react";
import './DatabaseConnector.css';

export default function DatabaseConnector({ setSchema, setConnectionString }) {
  const [conn, setConn] = useState("");
  const [loading, setLoading] = useState(false);

  const connectDB = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:5000/api/ingest/database", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ connection_string: conn })
      });
      const json = await res.json();
      if (json.status === "success") {
        setSchema(json.schema);
        setConnectionString(conn);
      } else {
        alert("Error: " + json.message);
      }
    } catch (err) {
      alert("Error: " + err);
    }
    setLoading(false);
  };

  return (
    <div className="database-connector">
      <h2>Database Connector</h2>
      <input
        className="input-field"
        value={conn}
        onChange={(e) => setConn(e.target.value)}
        placeholder="Enter connection string"
      />
      <button className="connect-btn" onClick={connectDB} disabled={loading}>
        {loading ? "Connecting..." : "Connect"}
      </button>
    </div>
  );
}