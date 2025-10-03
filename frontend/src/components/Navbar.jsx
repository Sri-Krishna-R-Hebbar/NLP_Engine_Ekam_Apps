import React from "react";
import { Link } from "react-router-dom";
import './Navbar.css';

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">NLP Engine</div>
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/database">Database Connect</Link>
        <Link to="/upload">Upload Docs</Link>
        <Link to="/query">Run Query</Link>
      </div>
    </nav>
  );
}