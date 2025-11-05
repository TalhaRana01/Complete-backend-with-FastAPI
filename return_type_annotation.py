from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel


app = FastAPI(title="Talha Rana AI Engineer")

@app.get("/product")
async def get_product():
  # return "hello world"  ## return simple string
  # return {"status": "OK"} ## return JSON key value
  return [
    {"message" : "Get all product"},
    {"status": "OK"}
    ]   ## return JSON in List