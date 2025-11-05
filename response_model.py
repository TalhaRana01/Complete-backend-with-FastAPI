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

# # without response_model parameters 
# @app.get("/product")
# async def get_product() :
#   # return { "id": 2, "name": "mobile", "price": 20000, "stock": 20}
#   return "hello world"

# with response_model parameters
# @app.get("/product", response_model=Product)
# async def get_product() :
#   # return { "id": 2, "name": "mobile", "price": 20000, "stock": 20}
#   return "hello world" ## ❌ doesn't return any data

# @app.get("/product", response_model=List[Product])
# async def get_product() :
#   return [
#     { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
#     { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
#     { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
#   ]

class BaseUser(BaseModel):
  username : str
  full_name : str
  
class UserIn(BaseUser):
  password : str


# # with return type
@app.post("/users")
async def create_user(user : UserIn) -> BaseUser:
  return user 
   
  