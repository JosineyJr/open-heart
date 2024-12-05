from pydantic import BaseModel
from typing import List, Dict


class RetrainInput(BaseModel):
    Age: int
    Sex: str 
    ChestPainType: str
    RestingBP: float
    Cholesterol: float
    FastingBS: int
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str
    HeartDisease: int

    def to_array(self):
        return [
            self.Age,
            self.Sex,
            self.ChestPainType,
            self.RestingBP,
            self.Cholesterol,
            self.FastingBS,
            self.RestingECG,
            self.MaxHR,
            self.ExerciseAngina,
            self.Oldpeak,
            self.ST_Slope,
            self.HeartDisease,
        ]
