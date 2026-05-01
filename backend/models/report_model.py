from pydantic import BaseModel

class TestResult(BaseModel):
    name: str
    value: float
    unit: str
    normal_range: str
    status: str
    explanation: str