from fastapi import FastAPI
from app.ml.model import predict_tendency
from app.ml.train import train_model
from app.schemas.prediction import PredictionInput
from app.schemas.retrain import RetrainInput
from app.ml.utils import append_to_csv, preprocess_data
from app.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_accuracy = "87.32%"


@app.post("/predict")
def predict(input_data: PredictionInput):
    prediction = predict_tendency(input_data.to_array())
    print(type(prediction))
    return {"tendency": prediction.tolist()[0]}


@app.post("/retrain")
def retrain(input_data: RetrainInput):
    global current_accuracy
    append_to_csv(settings.training_data_path, input_data=input_data)

    forecaster, target = preprocess_data()

    accuracy = train_model(forecaster, target)
    current_accuracy = "%.2f%%" % (accuracy * 100.0)
    return {"accuracy": current_accuracy}


@app.get("/accuracy")
def accuracy():
    global current_accuracy
    return {"accuracy": current_accuracy}
