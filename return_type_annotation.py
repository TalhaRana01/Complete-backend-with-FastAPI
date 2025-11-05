from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel


app = FastAPI(title="Talha Rana AI Engineer")

@app.get("/product")
async def get_product():
  return "hello world"