// components/Home.jsx
import React from "react";
import './Home.css';

export default function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to NLP Engine</h1>
      <p>Query your databases and documents with ease.</p>
      <div className="home-buttons">
        <a href="/database" className="btn">Connect Database</a>
        <a href="/upload" className="btn">Upload Documents</a>
        <a href="/query" className="btn">Run Query</a>
      </div>
    </div>
  );
}
