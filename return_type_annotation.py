from fastapi import FastAPI
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI(title="Talha Rana AI Engineer")

##---------------------------------------------------------------------------------------
# Return type Annotation sy hum return data ko validate kr skty hain restrict kr sty hain
##---------------------------------------------------------------------------------------


# # without return type
# @app.get("/product")
# async def get_product():
#   # return "hello world"    ## ✅ return simple string
#   # return {"status": "OK"} ## ✅  return JSON key value
#   return [
#     {"message" : "Get all product"},
#     {"status": "OK"}
#     ]                       ## ✅ return JSON in List

## Return type annotation 

class Product(BaseModel):
  id: int
  name : str
  price : float
  stock : int | None = None
  
## return only JSON Value
# @app.get("/product")
# async def get_product() -> Product:
#   # return "hello world" ## ❌ can't return simple string 
#   # return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}     ## ✅ Only return Product defined basemodel
#   return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}


# # Return JSON Value in List
@app.get("/product")
async def get_product() -> List[Product]:
  # return "hello world" ## ❌ can't return simple string 
  # return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}     ## ✅ Only return Product defined basemodel
  return [
    { "id": 1, "name": "laptop", "price": 20000, "stock": 25},
    { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
    { "id": 3, "name": "laptop", "stock": 50, "price": 20000,}
  ]