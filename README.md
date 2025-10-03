# NLP Query Engine for Employee Data

**A natural language query system for employee databases, dynamically adapting to any schema and supporting both structured and unstructured data.**

![Project Demo](https://via.placeholder.com/800x400?text=Demo+Video+Placeholder)

## 📌 Overview

This project is a **full-stack web application** that allows users to:

- Connect to any employee database and **auto-discover its schema**.
- Upload and process **unstructured documents** (PDFs, CSVs, etc.).
- Query the data using **natural language** and get results from both structured and unstructured sources.
- Visualize the schema, track performance, and export results.

Built for the **Ekam Labs AI Engineering Assignment**, this solution is **schema-agnostic**, production-ready, and optimized for performance.

---

## 🚀 Features

### Core Functionality

- **Dynamic Schema Discovery**: Automatically detects tables, columns, and relationships.
- **Natural Language Query Processing**: Supports SQL, document search, and hybrid queries.
- **Document Processing**: Handles PDFs, DOCX, TXT, and CSV files with intelligent chunking.
- **Performance Optimizations**: Caching, connection pooling, and async operations.

### User Interface

- **Data Ingestion Panel**: Connect to databases and upload documents.
- **Query Interface**: Auto-suggestions, query history, and real-time results.
- **Results Display**: Tables for structured data, cards for documents.
- **Metrics Dashboard**: Response time, cache hit rate, and active connections.

---

## 🛠️ Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Backend          | FastAPI (Python)      |
| Frontend         | React.js              |
| Database         | PostgreSQL/MySQL      |
| Embeddings       | Sentence Transformers |
| Caching          | Redis (optional)      |
| Document Parsing | PyPDF2, python-docx   |

---

## 📦 Project Structure

   NLP_ENGINE_EKAM_APPS
		├── backend/
		│   ├── api/
		│   │   ├── models/
		│   │   └── routes/
		│   │       ├──__pycache__/
		│   │       ├── debug.py
		│   │       ├── ingestion.py
		│   │       ├── query.py
		│   │       └── schema.py
		│   ├── services/
		│   │   ├── __pycache__/
		│   │   ├── document_processo...py
		│   │   ├── query_engine.py
		│   │   └── schema_discovery.py
		│   ├── tests/
		│   ├── uploads/
		│   ├── venv/
		│   ├── main.py
		│   └── requirements.txt
		├── frontend/
		│   ├── node_modules/
		│   ├── public/
		│   └── src/
		│       ├── components/
		│       │   ├── DatabaseConnector.jsx
		│       │   ├── DocumentUploader.jsx
		│       │   ├── QueryPanel.jsx
		│       │   └── ResultsView.jsx
		│       ├── App.css
		│       ├── App.jsx
		│       ├── App.test.js
		│       ├── index.css
		│       ├── index.js
		├── .gitignore
		├── package-lock.json
		├── package.json
		└── README.md

## 📥 Setup & Installation

### Prerequisites

- Python 3.8+
- Node.js (v16+)
- PostgreSQL/MySQL (or SQLite for demo)
- Redis (optional, for caching)

---

### Backend Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Sri-Krishna-R-Hebbar/NLP_Engine_Ekam_Apps.git
cd NLP_Engine_Ekam_Apps/backend`
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the backend:**

```bash
python main.py
```

- The backend will start at http://localhost:8000.

---

### Frontend Setup

1. **Navigate to the frontend directory:**

```bash
cd ../frontend
```

2. **Install dependencies:**

```bash
npm install
```

3. **Run the frontend:**

```bash
npm start
```

- The frontend will start at http://localhost:3000.


## 🎯 Usage

### 1. Data Ingestion

* **Connect to a Database** :

  * Enter your database connection string in the **Database Connector** panel.
  * Click **Test Connection** to auto-discover the schema.
* **Upload Documents** :

  * Drag and drop files (PDF, DOCX, CSV) into the  **Document Uploader** .
  * Monitor progress in real-time.

### 2. Query Data

* Enter a natural language query (e.g.,  *"Show me all Python developers in Engineering"* ).
* View results in **table format** (structured data) or **cards** (documents).
