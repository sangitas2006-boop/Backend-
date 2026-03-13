from fastapi import FastAPI
import pandas as pd

app = FastAPI()

data = pd.read_csv("pipeline_leakage_dataset.csv")

index = 0

@app.get("/")
def home():
    return {"message": "Smart Water Pipeline Monitoring API"}

@app.get("/sensor-data")
def sensor_data():

    global index

    row = data.iloc[index]

    index += 1

    if index >= len(data):
        index = 0

    return {
        "water_speed": float(row["water_speed_mps"]),
        "pressure": float(row["pipeline_pressure_bar"]),
        "moisture": float(row["ground_moisture_percent"]),
        "vibration": float(row["pipe_vibration"]),
        "leakage": int(row["leakage"])
    }
