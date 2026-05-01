import os
import uuid
from fastapi import APIRouter, UploadFile, File

from services.ocr_service import clean_text, extract_text
from services.parse_service import map_test_name, parse_value, parse_medical_report
from services.rule_engine import evaluate_status
from services.llm_service import generate_explanation

router = APIRouter()

# Ensure uploads directory exists
UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze-report")
async def analyze_report(file: UploadFile = File(...)):
    # Save uploaded file
    file_ext = os.path.splitext(file.filename)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Extract text from uploaded file using OCR
    raw_text = extract_text(file_path)
    
    if not raw_text:
        return {
            "tests": [],
            "overall_analysis": "Could not extract text from file. Please try a clearer image.",
            "recommendations": ["Ensure the image is clear and readable"]
        }
    
    # Parse the extracted text into structured data
    raw_data = parse_medical_report(raw_text)
    
    results = []

    for item in raw_data:
        clean_name = clean_text(item["name"])
        test_name = map_test_name(clean_name)
        
        value = parse_value(test_name, item["value"])
        status = evaluate_status(test_name, value)
        explanation = generate_explanation(test_name, value, status)

        results.append({
            "name": test_name,
            "value": value,
            "status": status,
            "explanation": explanation
        })
    
    # Clean up uploaded file after processing
    try:
        os.remove(file_path)
    except:
        pass

    return {
        "tests": results,
        "overall_analysis": "Processed successfully",
        "recommendations": [
            "Consult doctor if abnormal values detected"
        ]
    }
