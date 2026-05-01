# Medical Report Analyzer

An AI-powered application that analyzes medical reports (lab reports, diagnostic reports) using OCR and LLM technology to extract, parse, and analyze medical test values with health recommendations.

## Features

- **OCR Processing**: Extract text from medical report images using Tesseract OCR
- **Intelligent Parsing**: Parse medical test values, reference ranges, and units
- **Health Analysis**: Analyze test values against reference ranges
- **AI-Powered Insights**: Get health recommendations using LLM (OpenAI GPT)
- **Modern UI**: Clean, responsive React-based frontend

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Tesseract OCR** - Optical Character Recognition
- **OpenAI GPT** - AI language model for health insights
- **Pillow & OpenCV** - Image processing

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **CSS** - Styling

## Project Structure

```
medical-report-analyzer/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── models/             # Data models
│   │   └── report_model.py
│   ├── routes/             # API routes
│   │   └── analyze.py
│   ├── services/           # Business logic
│   │   ├── ocr_service.py      # OCR processing
│   │   ├── parse_service.py    # Text parsing
│   │   ├── analyzer_service.py # Analysis engine
│   │   ├── rule_engine.py      # Health rules
│   │   ├── llm_service.py      # OpenAI integration
│   │   └── genai_service.py   # Google GenAI
│   ├── utils/              # Utilities
│   │   ├── helpers.py
│   │   └── medical_dictionary.py
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── UploadForm.jsx
│   │   │   ├── ResultTable.jsx
│   │   │   └── Summary.jsx
│   │   ├── api.js         # API client
│   │   ├── App.jsx       # Main app
│   │   ├── main.jsx      # Entry point
│   │   └── styles.css    # Styles
│   ├── package.json     # Node dependencies
│   └── index.html      # HTML template
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- Tesseract OCR installed

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
# OpenAI API Key (required for AI insights)
OPENAI_API_KEY=your-openai-api-key

# Optional: Google Generative AI API Key
GOOGLE_API_KEY=your-google-api-key
```

### Tesseract OCR Setup

1. **Windows**: Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. **Mac**: `brew install tesseract`
3. **Linux**: `sudo apt install tesseract-ocr`

## Running the Application

### Start Backend Server

```bash
cd backend
uvicorn app:app --reload
```

The backend will be available at `http://localhost:8000`

### Start Frontend Development Server

```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:5173`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/analyze` | POST | Upload and analyze medical report |
| `/api/health` | GET | Health check |

## Usage

1. Open the frontend in your browser
2. Upload a medical report image (JPG, PNG, or PDF)
3. Wait for OCR processing to complete
4. View parsed test results in the table
5. Read AI-powered health insights and recommendations

## License

MIT License

## Author

Kishor Kumar
