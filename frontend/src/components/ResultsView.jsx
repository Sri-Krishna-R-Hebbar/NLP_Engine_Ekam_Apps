// components/ResultsView.jsx
import React from "react";
import './ResultsView.css';

export default function ResultsView({ results }) {
  return (
    <div className="results-view">
      <h2>Results</h2>
      <div className="database-results">
        <h3>Database Results:</h3>
        {results.results && results.results.length ? (
          <pre>{JSON.stringify(results.results, null, 2)}</pre>
        ) : (
          <p>No database results found.</p>
        )}
      </div>
      <div className="document-results">
        <h3>Document Answer:</h3>
        {results.documents && results.documents.length ? (
          <ul>
            {results.documents.map((doc, i) => (
              <li key={i}>{doc}</li>
            ))}
          </ul>
        ) : (
          <p>No relevant documents found.</p>
        )}
      </div>
    </div>
  );
}