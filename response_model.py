from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Talha Rana AI Engineer")


class Product(BaseModel):
  id : int
  name : str
  price : float
  stock : int | None = None
  
class ProductOut(BaseModel):
  name : str
  price : float

# # without response model parameters 
@app.get("/product")
async def get_product() :
  return { "id": 2, "name": "mobile", "price": 20000, "stock": 20}