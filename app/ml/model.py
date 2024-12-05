import pickle
import numpy as np
from xgboost import XGBClassifier
from app.config.settings import settings


def predict_tendency(data):
    forecaster = open(settings.forecaster_path, "rb")
    forecaster = pickle.load(forecaster)
    target = open(settings.target_path, "rb")
    target = pickle.load(target)

    xg = XGBClassifier(
        max_depth=2,
        learning_rate=0.05,
        n_estimators=250,
        objective="binary:logistic",
        random_state=3,
    )
    xg.fit(forecaster, target)

    prediction = xg.predict([data])
    return prediction
