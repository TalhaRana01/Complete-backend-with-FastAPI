from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


app = FastAPI()

# @app.get("/")
# async def home():
#   return {"message" : "Talha Rana"}


# ------------------------------------------------------------------------------------------------------
## Path Parameters 
# ------------------------------------------------------------------------------------------------------

# Get Request 
## Read or fetch All data

# @app.get("/product")
# async def all_product():
#   return  {"message" : "All products list"}

# GET Request 

## Read single product by id
# @app.get("/product/{product_id}")
# async def product(product_id : int):
#   return  {"product ID" : product_id}

## Pydantic 

# class Product(BaseModel):
#   name : str
#   price : float
  

# POST Request

# Create a product
# @app.post("/product")
# async def create_product(new_product: dict):
#   return {"message" : "Product is created", "product" : new_product}


# Create a product
# @app.post("/product")
# async def create_product(new_product: Product):
#   return {"message" : "Product is created", "product" : new_product}


# @app.put("/product/{product_id}")
# async def update_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}

# @app.patch("/product/{product_id}")
# async def partial_update_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


# @app.delete("/product/{product_id}")
# async def delete_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


# Get Method 

# @app.get("/")
# def home():
#   return {"response" : "Home Page "}

# # Get all products
# @app.get("/product")
# def get_product():
#   return {"message" : "Get All Products Method"}

# Post Method

# @app.post("/product/{product_id}")
# def create_product(product_id : int, new_product : dict):
#   return {"product id" :product_id, "product" : new_product}


# @app.patch("/product/{product_id}")
# async def partial_update_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


# @app.put("/product/{product_id}")
# async def update_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


# @app.delete("/product/{product_id}")
# async def delete_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


### ------------------------------------------------------------------------------------------------------
## Parameter with Type
### ------------------------------------------------------------------------------------------------------



 
# @app.get("/product/{product_id}")
# def get_single_product(product_id: int,  ):
#   return {"response" : "Single Product ID", "product_id" : product_id }


### ------------------------------------------------------------------------------------------------------
## Predefined Value
### ------------------------------------------------------------------------------------------------------


class ProductCategory(str, Enum):
  books = "Books"
  clothing = "Clothing"
  electronic = "Electronic"

@app.get("/product/{category}")
async def get_product(category : ProductCategory):
  return {"response" : "Product Fetched", "category" : category}


### ------------------------------------------------------------------------------------------------------
## Working with python enumerations
### ------------------------------------------------------------------------------------------------------

class ProductCategory(str, Enum):
  books = "books"
  clothing = "clothing"
  electronic = "electronic"
  
@app.get("/product/{category}")
async def get_product(category : ProductCategory):
  if category == ProductCategory.books:
    return {"category" : category}
  
  elif category.value == 'clothing':
    return {"category" : category}
  
  elif category == ProductCategory.electronic.value:
    return {"category" : category}
  else:
    return {"message" : "Unknow catgory"}