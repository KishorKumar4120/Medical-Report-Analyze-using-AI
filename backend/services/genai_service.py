import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_explanation(test: dict) -> str:
    prompt = f"""
    Explain this medical test in simple language:

    Test: {test['name']}
    Value: {test['value']} {test['unit']}
    Normal Range: {test['normal_range']}
    Status: {test['status']}

    Explain:
    - What it means
    - Possible causes
    - Simple advice
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return "Explanation not available"