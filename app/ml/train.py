import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

def train_model(forecaster, target):
    x_train, x_teste, y_train, y_teste = train_test_split(
        forecaster, target, test_size=0.3, random_state=0
    )

    model = XGBClassifier(
        max_depth=2,
        learning_rate=0.05,
        n_estimators=250,
        objective="binary:logistic",
        random_state=3,
    )
    model.fit(x_train, y_train)
    
    accuracy = accuracy_score(y_teste, model.predict(x_teste))

    return accuracy
