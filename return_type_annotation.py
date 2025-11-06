from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI(title="Talha Rana AI Engineer")

##---------------------------------------------------------------------------------------
# Return type Annotation sy hum kisi bhi function ka return data ko validate kr skty hain restrict kr sty hain
##---------------------------------------------------------------------------------------


# # without return type
# @app.get("/product" )
# async def get_product():
#   ## ✅ return simple string
#   # return "hello world"  
#   ## ✅ return JSON key value  
#   # return {"status": "OK"} 
#   ## ✅ return List of JSON
#   return [
#     {"message" : "Get all product"},
#     {"status": "OK"}
#     ]                       
  
  ## ✅ return complete simple HTML form  with response_class=HTMLResponse 
  # return """
  #   <html>
  #     <body>
  #       <h2>Login Form</h2>
  #       <form action="/login/" method= "post">
  #           <label for="username">username</label><br>
  #           <input type="text" id="username" name="username"><br>
  #           <label for="password">password</label><br>
  #           <input type="password" id="password" name="password"><br>
  #           <input type="submit"  value="submit">
  #       </form>
  #     </body>
  #   </html>"""

## Return type annotation 

# class Product(BaseModel):
#   id: int
#   name : str 
#   price : float
#   stock : int | None = None
  
## return only JSON Value
# @app.get("/product")
# async def get_product() -> Product:
#   # return "hello world" ## ❌ can't return simple string 
#   # return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}     ## ✅ Only return Product defined basemodel
#   return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}


# # Return JSON Value in List
# @app.get("/product")
# async def get_product() -> List[Product]:
  # return "hello world" ## ❌ can't return simple string 
  # return { "id": 1, "name": "laptop", "price": 20000, "stock": 25}     ## ❌ do not return Product defined basemodel
  # return [
  #   { "id": 1, "name": "laptop", "price": 20000, "stock": 25},
  #   { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
  #   { "id": 3, "name": "laptop", "stock": 50, "price": 20000,}
  # ]                                                                       ## ✅ Only return list of product defined basemodel


## without return type annotation 
# @app.post("/product")
# async def create_product(product: Product):
  # return product   ## ✅ return product basemodel in response body
  # return "This is a product" ## ✅ return simple String in response body
 
    
  
  
## with return type annotation  
# @app.post("/product")
# async def create_product(product:Product) -> Product:
#   # return product   ## ✅ return product basemodel in response body
#   return "This is a product" ## ❌do not  return simple String in response body
#   # return [
#   #   { "id": 1, "name": "laptop", "price": 20000, "stock": 25},
#   #   { "id": 2, "name": "mobile", "price": 20000, "stock": 20},
#   #   { "id": 3, "name": "laptop", "stock": 50, "price": 20000,}
    
#   # ]


class Product(BaseModel):
  name : str
  price : float
  
  
  
class ProductOut(Product):
  id : int
  name : str
  price : float
  stock : int | None = None
  
  
# Restricted data 
# function input is Product id, name, price and stock
# function return or output name, and price
@app.post("/product")
async def get_product(product: ProductOut) -> Product:
  return product

# User Password restricted to return
# class BaseUser(BaseModel):
#  username: str
#  full_name : str | None = None
  
# class UserIn(BaseUser):
#   password : str
  
  
  
# ## Restricted data 
# ## function input is Product id, name, price and stock
# ## function return or output name, and price
# @app.post("/user")
# async def create_user(user: UserIn) -> BaseUser:
#   return user
  
  