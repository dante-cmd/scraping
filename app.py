import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ['localhost',
  "http://localhost",
    "http://localhost:8080","http://127.0.0.1:5502"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/')

async def index():
    numbers = np.random.randn(5)
    numbers_list = numbers.tolist()
    return {"number":numbers_list}