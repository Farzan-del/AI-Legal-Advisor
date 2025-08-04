⚖️ Legal Document Analyzer & RAG Assistant

This project is an AI-powered legal case analysis system that extracts structured information from DOCX legal case files, generates human-readable criminal reports, performs semantic legal research, and supports Retrieval-Augmented Generation (RAG)-based Q&A with integration of LLMs such as OpenAI or Gemini.

## Features

###  Document Upload & Analysis
- Upload `.docx` legal documents
- Extract structured case data (e.g., name, crime, location, date)
- Automatically generate a professional criminal report
- Identify and display relevant **Pakistan Penal Code (PPC)** sections
- Provide legal research context based on the extracted crime

### Legal RAG Assistant (LLM-Powered)
- Ask legal questions about PPC or case-specific context
- Uses RAG architecture: vector search + LLM for accurate and contextual answers
- Backend handles semantic search using ChromaDB or FAISS
- Integrates with OpenAI GPT or Gemini Pro LLMs

---

## Tech Stack

### Backend
- **Python**
- **FastAPI** – For high-performance API routes
- **SQLAlchemy** – ORM for database interaction
- **SQLite / PostgreSQL** – For storing case and user query data

### NLP / AI
- **OpenAI GPT / Gemini Pro** – For generating legal Q&A and summaries
- **FAISS / ChromaDB** – Vector search for RAG implementation

### Document Parsing
- **python-docx** – For extracting data from `.docx` files
- **PyMuPDF** – To read text from PDF documents
- **Tesseract OCR** – For scanned or image-based legal documents

### Frontend
- **Streamlit** – For interactive web UI
- **Custom HTML/CSS** – For enhanced UI styling

---

## Project Structure
LEGAL_ADVISOR_PROJECT/
├── App/
│ ├── api_main.py # FastAPI backend
│ ├── agent1_extract.py # Extract structured data from DOCX
│ ├── agent2_report_gen.py # Generate criminal report
│ ├── agent3_research.py # Legal research output
│ ├── agent4_ppc_matcher.py # Match crime to PPC sections
│ ├── rag_assistant.py # RAG pipeline using vector DB + LLM
│ └── db.py # DB schema and ORM setup
├── streamlit_app.py # Frontend UI built with Streamlit
├── requirements.txt # Dependencies
└── README.md # Project documentation

