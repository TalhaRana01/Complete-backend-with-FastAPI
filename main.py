from fastapi import FastAPI
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

class Product(BaseModel):
  name : str
  price : float
  

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

@app.get("/")
def home():
  return {"response" : "Home Page "}

# Get all products
@app.get("/product")
def get_product():
  return {"message" : "Get All Products Method"}

# Post Method

@app.post("/product/{product_id}")
def create_product(product_id : int, new_product : dict):
  return {"product id" :product_id, "product" : new_product}


@app.patch("/product/{product_id}")
async def partial_update_product(new_update_product : Product, product_id: int):
  return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


@app.put("/product/{product_id}")
async def update_product(new_update_product : Product, product_id: int):
  return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


@app.delete("/product/{product_id}")
async def delete_product(new_update_product : Product, product_id: int):
  return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


