from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Talha Rana AI Engineer")


@app.get("/")
def get():
  return "Talha Rana AI Engineer"