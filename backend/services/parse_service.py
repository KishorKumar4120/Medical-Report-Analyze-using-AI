import re
from utils.medical_dictionary import MEDICAL_MAP

def map_test_name(raw_name: str):
    raw_name = raw_name.lower().strip()
    return MEDICAL_MAP.get(raw_name, raw_name.title())


def parse_value(name, value):
    # FIX BLOOD PRESSURE BUG
    if name == "Blood Pressure":
        s = str(value)

        # handle wrong OCR like 120780 → 120/80
        if "/" not in s and len(s) == 6:
            return f"{s[:3]}/{s[3:]}"
        return s

    return value

def parse_medical_report(text: str) -> list:
    lines = text.split("\n")
    results = []

    pattern = r"([A-Za-z ]+)\s+([\d.]+)\s*(g/dL|mg/dL|mmol/L)?\s*([\d.]+-?[\d.]*)?"

    for line in lines:
        match = re.search(pattern, line)
        if match:
            name = match.group(1).strip()
            value = float(match.group(2))
            unit = match.group(3) if match.group(3) else ""
            normal_range = match.group(4) if match.group(4) else ""

            results.append({
                "name": name,
                "value": value,
                "unit": unit,
                "normal_range": normal_range
            })

    return results