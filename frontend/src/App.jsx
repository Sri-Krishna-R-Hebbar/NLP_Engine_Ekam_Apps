import React, { useState } from "react";
import DatabaseConnector from "./components/DatabaseConnector";
import DocumentUploader from "./components/DocumentUploader";
import QueryPanel from "./components/QueryPanel";
import ResultsView from "./components/ResultsView";
import "./App.css";

export default function App() {
  const [schema, setSchema] = useState(null);
  const [results, setResults] = useState({ results: [], documents: [] });
  const [connectionString, setConnectionString] = useState("");
  const [showResults, setShowResults] = useState(false);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>📚 NLP Database Query Engine</h1>
        <p className="subtitle">Query your database and documents intelligently</p>
      </header>

      <main className="app-main">
        <section className="card">
          <h2>Connect to Database</h2>
          <DatabaseConnector
            setSchema={setSchema}
            setConnectionString={setConnectionString}
          />
        </section>

        <section className="card">
          <h2>Upload Documents</h2>
          <DocumentUploader />
        </section>

        <section className="card">
          <h2>Run Query</h2>
          <QueryPanel
            connectionString={connectionString}
            setResults={setResults}
            setShowResults={setShowResults}
          />
        </section>

        {showResults && (
          <section className="card results-card">
            <h2>Query Results</h2>
            <ResultsView results={results} />
          </section>
        )}
      </main>

      <footer className="app-footer">
        <p>© 2025 NLP Engine • Built with ❤️ by Sri Krishna</p>
      </footer>
    </div>
  );
}
