from pydantic import BaseModel


class PredictionInput(BaseModel):
    Age: int
    Sex: int 
    ChestPainType: int
    RestingBP: float
    Cholesterol: float
    FastingBS: int
    RestingECG: int
    MaxHR: int
    ExerciseAngina: int
    Oldpeak: float
    ST_Slope: int

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
        ]
