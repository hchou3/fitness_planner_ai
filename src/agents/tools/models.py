from pydantic import BaseModel

class UserStats(BaseModel):
    age: int
    height: float
    weight: float
    unit: str
    activity: str
    goal: str

class ProgramSuggestion(BaseModel):
    program_type: str
    weeks: int
    summary: str

class Confirmation(BaseModel):
    accepted: bool
    additional_info: str = ""
