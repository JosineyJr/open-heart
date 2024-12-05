import pandas as pd
from app.schemas.retrain import RetrainInput
from app.config.settings import settings


def append_to_csv(file_path: str, input_data: RetrainInput):
    data_dict = {
        "Age": input_data.Age,
        "Sex": input_data.Sex,
        "ChestPainType": input_data.ChestPainType,
        "RestingBP": input_data.RestingBP,
        "Cholesterol": input_data.Cholesterol,
        "FastingBS": input_data.FastingBS,
        "RestingECG": input_data.RestingECG,
        "MaxHR": input_data.MaxHR,
        "ExerciseAngina": input_data.ExerciseAngina,
        "Oldpeak": input_data.Oldpeak,
        "ST_Slope": input_data.ST_Slope,
        "HeartDisease": input_data.HeartDisease,
    }

    # Convert the dictionary into a DataFrame
    new_data = pd.DataFrame([data_dict])

    try:
        # Attempt to read the existing CSV file with ';' delimiter
        df = pd.read_csv(file_path, delimiter=';')
    except FileNotFoundError:
        # If the file does not exist, create an empty DataFrame with columns
        df = pd.DataFrame(columns=data_dict.keys())

    # Concatenate the new data to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated DataFrame to CSV with ';' delimiter
    df.to_csv(file_path, sep=';', index=False)
    print(f"Data appended to {file_path}")


def preprocess_data():
    pd.set_option("future.no_silent_downcasting", True)

    df = pd.read_csv(settings.training_data_path, sep=";", encoding="utf-8")

    df["Sex"] = df["Sex"].infer_objects(copy=False).replace({"M": 0, "F": 1})
    df["ChestPainType"] = (
        df["ChestPainType"]
        .infer_objects(copy=False)
        .replace({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    )
    df["RestingECG"] = (
        df["RestingECG"]
        .infer_objects(copy=False)
        .replace({"Normal": 0, "ST": 1, "LVH": 2})
    )
    df["ExerciseAngina"] = (
        df["ExerciseAngina"].infer_objects(copy=False).replace({"N": 0, "Y": 1})
    )
    df["ST_Slope"] = (
        df["ST_Slope"]
        .infer_objects(copy=False)
        .replace({"Up": 0, "Flat": 1, "Down": 2})
    )

    forecaster = df.iloc[:, 0:11].values
    target = df.iloc[:, 11].values

    return forecaster, target
