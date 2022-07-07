from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {
        "08:00": {"weather": "cloudy", "temperature": "25°C"}
    }


