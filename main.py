from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Water Pipeline Monitoring API"}

# load dataset safely
try:
    data = pd.read_csv("pipeline_leakage_dataset.csv")
except Exception as e:
    data = None
    print("CSV ERROR:", e)

index = 0

@app.get("/sensor-data")
def sensor_data():
    global index

    if data is None:
        return {"error": "Dataset not loaded"}

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
