import uvicorn
import pickle
import pandas
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
from sklearn.preprocessing import StandardScaler

app = FastAPI()

with open("models/model_airflow.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
async def read_root() -> JSONResponse:
    return JSONResponse(content={"health": "ok"})


@app.post("/predict")
async def predict(request: Request) -> JSONResponse:
    try:
        data = await request.json()
        data = pandas.DataFrame(data, index=[0])
        data = data[['latitude', 'longitude', 'velocity', 'altitude']]
        scaler = StandardScaler()
        data = scaler.fit_transform(data)
        prediction = model.predict(data)
        return JSONResponse(content={"prediction": str(prediction[0])})
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
