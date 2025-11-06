from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Any, Optional


app = FastAPI(title="Talha Rana AI Engineer")


class Product(BaseModel):
  id : int
  name : str
  price : float
  stock : int | None = None
  
class ProductOut(BaseModel):
  name : str
  price : float

# without response_model parameters 
# @app.get("/product")
# async def get_product() :
#   # return { "id": 2, "name": "mobile", "price": 20000, "stock": 20}  ✅ return
#   # return "hello world"  ✅ return

# @app.get("/user", response_class=HTMLResponse)
# def get_user():
#     return """
#     <html>
#       <body>
#         <h2>Login Form</h2>
#         <form action="/login/" method= "post">
#             <label for="username">username</label><br>
#             <input type="text" id="username" name="username"><br>
#             <label for="password">password</label><br>
#             <input type="password" id="password" name="password"><br>
#             <input type="submit"  value="submit">
#         </form>
#       </body>
#     </html>"""

## with response_model parameters
# @app.get("/product", response_model=Product)
# async def get_product() :
#   # return { "id": 2, "name": "mobile", "price": 20000, "stock": 20}
#   # return "hello world" ## ❌ doesn't return any data


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


# # with return type annotation
@app.post("/users")
async def create_user(user : UserIn) -> BaseUser:
  return user 

## with response_model 
# @app.post("/users", response_model= BaseUser)
# async def create_user(user : UserIn) -> BaseUser:
#   return user 

## with return type annotation and response_model 
# @app.post("/users", response_model= BaseUser)
# async def create_user(user : UserIn) -> Any:
#   return user 

## response_model None foe disable
# @app.post("/users", response_model= None)
# async def create_user(user : UserIn) -> Any:
  # return user 

## -------------------------------------------------
#  Include and Exlude unset dafauly vaues
## -------------------------------------------------



# product_db = {
#   "1" : { "id": 1, "name": "mobile", "price": 20000, "stock": 20, "is_active": True},
#   "2" : { "id": 2, "name": "laptop", "price": 50000, "stock": 20, "is_active": False},
  
# }

# print(type(product_db))

# class Product(BaseModel):
#   id : int
#   name : str
#   price : float 
#   description : Optional[str] = None
#   tax: float = 15.0  # Default tax rate
  
# @app.get("/products/{product_id}", response_model=Product, response_model_exclude_unset=True)
# async def get_product(product_id: str):
#   return product_db.get(product_id, {})

## Including Specific Fields
# @app.get("/products/{product_id}", response_model=Product, response_model_include={"name", "price"})
# async def get_product(product_id: str):
#   return product_db.get(product_id, {})

## Excluding Specific Fields with response_model_exclude
# @app.get("/products/{product_id}", response_model=Product, response_model_exclude={"name", "price"})
# async def get_product(product_id: str):
#   return product_db.get(product_id, {})