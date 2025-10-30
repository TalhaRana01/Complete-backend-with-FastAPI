from fastapi import FastAPI
from typing import Dict, Annotated
from pydantic import BaseModel


app = FastAPI(title= "Talha Rana Professional AI Engineer ")


@app.post("/products")
async def create_product(new_product : dict):
  
  return new_product 