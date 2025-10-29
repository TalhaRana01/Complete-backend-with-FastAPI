from fastapi import FastAPI, status, Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated


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


# class ProductCategory(str, Enum):
#   books = "Books"
#   clothing = "Clothing"
#   electronic = "Electronic"

# @app.get("/product/{category}")
# async def get_product(category : ProductCategory):
#   return {"response" : "Product Fetched", "category" : category}


### ------------------------------------------------------------------------------------------------------
## Working with python enumerations
### ------------------------------------------------------------------------------------------------------

# class ProductCategory(str, Enum):
#   books = "Books"
#   clothing = "Clothing"
#   electronic = "Electronic"
  
# @app.get("/product/{category}")
# async def get_product(category : ProductCategory):
#   if category == ProductCategory.books:
#     return {"category" : category}
  
#   elif category.value == 'clothing':
#     return {"category" : category}
  
#   elif category == ProductCategory.electronic.value:
#     return {"category" : category}
#   else:
#     return {"message" : "Unknow catgory"}


### ------------------------------------------------------------------------------------------------------
## CRUD Operation with dummy data
### ------------------------------------------------------------------------------------------------------

# PRODUCTS = [
#   {
#     "product_id": "FKP1001",
#     "product_name": "Turbo-Clean All-in-One Detergent",
#     "category": "Household Goods",
#     "price": 19.99,
#     "in_stock": True,
#     "description": "The revolutionary cleaner that promises to remove any stain instantly. Contains 'secret formula X.' (Warning: May leave a sticky residue.)"
#   },
#   {
#     "product_id": "FKP1002",
#     "product_name": "Eternal Youth Face Cream",
#     "category": "Cosmetics",
#     "price": 89.50,
#     "in_stock": False,
#     "description": "Instantly reduces the appearance of wrinkles by 100%. Side effects may include temporary, minor itching. Sold as a novelty item."
#   },
#   {
#     "product_id": "FKP1003",
#     "product_name": "Ultra-Power USB-C Cable (10ft)",
#     "category": "Electronics",
#     "price": 5.99,
#     "in_stock": True,
#     "description": "Guaranteed to charge your device 50% faster. Known to fail after three uses."
#   },
#   {
#     "product_id": "FKP1004",
#     "product_name": "Organic Gluten-Free Water",
#     "category": "Food & Drink",
#     "price": 3.49,
#     "in_stock": True,
#     "description": "The purest, most natural water, now with a 'certified organic' sticker. Tastes exactly like regular tap water."
#   },
#   {
#     "product_id": "FKP1005",
#     "product_name": "Invisible Wireless Headphones",
#     "category": "Electronics",
#     "price": 199.00,
#     "in_stock": False,
#     "description": "So small and seamless, you won't even know you're wearing them! (Because they're literally just an empty box.)"
#   }
# ]


# Get all products
# @app.get("/products", status_code=status.HTTP_200_OK)
# async def all_products():
#   return {"message" : PRODUCTS}


# # Get Single Product
# @app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
# async def get_single_product(product_id):
#   for product in PRODUCTS:
#     if product['product_id'] == product_id:
#       return product

# Create product  
# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: dict):
#   PRODUCTS.append(new_product)
#   return {"response" : "Product created ", "new_product": new_product}


# @app.put("/products/{product_id}")
# async def update_product(product_id, update_product: dict):
#   for index, product in enumerate(PRODUCTS):
#     if product['product_id'] == product_id:
#       PRODUCTS[index] = update_product
#       return {"response" : "Product updated", "product_id": product_id, "update_product" : update_product}
      
    


# @app.patch("/products/{product_id}")
# async def partial_update_product(product_id, update_product: dict):
#   for index, product in enumerate(PRODUCTS):
#     if product['product_id'] == product_id:
#       PRODUCTS[index] = update_product
#       return {"response" : "Product updated", "product_id": product_id, "update_product" : update_product}

# @app.delete("/products/{product_id}")
# async def delete_product(product_id,):
#   for index, product in enumerate(PRODUCTS):
#     if product['product_id'] == product_id:
#       PRODUCTS.pop(index)
#       return { "message" : " Product deleted", "deleted_product": delete_product}
  
  
  
### ------------------------------------------------------------------------------------------------------
## Query Parameters
### ------------------------------------------------------------------------------------------------------


### ------------------------------------------------------------------------------------------------------
## Single Query Parameters
### ------------------------------------------------------------------------------------------------------

# @app.get("/product")
# async def product(category:str):
#   return {"status" : "OK", "lan" : category}

# @app.get("/product")
# async def product(en:str):
#   return {"status" : "OK", "lan" : en}

# @app.get("/product")
# async def product(q:str):
#   return {"status" : "OK", "lan" : q}

# @app.get("/course")
# async def course(course: str):
#   return {"course" : course}


### ------------------------------------------------------------------------------------------------------
## Multi Query Parameters
### ------------------------------------------------------------------------------------------------------

# @app.get("/product")
# async def product(q:str, limit: int, en:str):
#   return {"status" : "OK", "lan" : q, "limit": limit, "lan" : en}


# @app.get("/course")
# async def course(course: str, type: bool):
#   return {"course" : course, "type": True}

### ------------------------------------------------------------------------------------------------------
## Default Query Parameters
### ------------------------------------------------------------------------------------------------------

# @app.get("/course")
# async def course(course: str, limit:int=10):
#   return {"course" : course, "limit": limit}

### ------------------------------------------------------------------------------------------------------
## Optional Query Parameters by assigning None 
### ------------------------------------------------------------------------------------------------------

# @app.get("/course")
# async def course(course: str, limit: int | None = None) :
#   return {"status": "OK", "course" : course, "limit": limit}

# @app.get("/course")
# async def course(limit: int, course: str | None = None) :
#   return {"status": "OK", "course" : course, "limit": limit}


# Path and Query Parameters
# @app.get("/product/{year}")
# async def product(year: str, category : str, limit: int) :
#   return {"status": "OK", "category" : category, "year" : year, "limit": limit}

# @app.get("/product/{year}")
# async def product(year: str, category : str | None = None, limit: int = 10) :
#   return {"status": "OK", "category" : category, "year" : year, "limit": limit}


### ------------------------------------------------------------------------------------------------------
## Response Status Code
### ------------------------------------------------------------------------------------------------------



# @app.post("/product", status_code=201)
# async def create_product(product: dict):
#   return product

# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(product: dict):
#   return product

# @app.get("/product", status_code=status.HTTP_200_OK)
# async def get_all_product():
#   return {"status" : "OK", "product": PRODUCTS}



### ------------------------------------------------------------------------------------------------------
## Basic Query Parameters
### ------------------------------------------------------------------------------------------------------

PRODUCTS = [
  {
    "product_id": "FKP1001",
    "product_name": "Turbo-Clean All-in-One Detergent",
    "category": "Household Goods",
    "price": 19.99,
    "in_stock": True,
    "description": "The revolutionary cleaner that promises to remove any stain instantly. Contains 'secret formula X.' (Warning: May leave a sticky residue.)"
  },
  {
    "product_id": "FKP1002",
    "product_name": "Eternal Youth Face Cream",
    "category": "Cosmetics",
    "price": 89.50,
    "in_stock": False,
    "description": "Instantly reduces the appearance of wrinkles by 100%. Side effects may include temporary, minor itching. Sold as a novelty item."
  },
  {
    "product_id": "FKP1003",
    "product_name": "Ultra-Power USB-C Cable (10ft)",
    "category": "Electronics",
    "price": 5.99,
    "in_stock": True,
    "description": "Guaranteed to charge your device 50% faster. Known to fail after three uses."
  },
  {
    "product_id": "FKP1004",
    "product_name": "Organic Gluten-Free Water",
    "category": "Food & Drink",
    "price": 3.49,
    "in_stock": True,
    "description": "The purest, most natural water, now with a 'certified organic' sticker. Tastes exactly like regular tap water."
  },
  {
    "product_id": "FKP1005",
    "product_name": "Invisible Wireless Headphones",
    "category": "Electronics",
    "price": 199.00,
    "in_stock": False,
    "description": "So small and seamless, you won't even know you're wearing them! (Because they're literally just an empty box.)"
  }
]

# @app.get("/products")
# async def products(search:str | None = None):
#   if search:
#     serach_lower = search.lower()
#     filtered_product = []
#     for product in PRODUCTS:
#       if serach_lower in product["product_name"].lower():
#         filtered_product.append(product)
       
#     return filtered_product
#   return PRODUCTS    



# Import Query from FastAPI for this code 

# Es code sy hum user query ko limit kr skty hain es method sy Query(default=None, max_length=5) old way to limit the query

# # Validation without Annotated
# @app.get("/products")
# async def products(search:str | None = Query(default=None, max_length=10)):
#   if search:
#     serach_lower = search.lower()
#     filtered_product = []
#     for product in PRODUCTS:
#       if serach_lower in product["product_name"].lower():
#         filtered_product.append(product)
       
#     return filtered_product
#   return PRODUCTS    


# Annotated method import krain ge typing module sy
# Validation with Annotated

# @app.get("/products")
# async def products(search: 
#   Annotated[
#     str | None, 
#     Query(max_length=10)
#     ] = None ):
  
#   if search:
#     serach_lower = search.lower()
#     filtered_product = []
#     for product in PRODUCTS:
#       if serach_lower in product["product_name"].lower():
#         filtered_product.append(product)
       
#     return filtered_product
#   return PRODUCTS    


# Why use Annotated ?
## FastAPI 0.95+ officially recommends using Annotated for dependencies and parameters


## REQUIRED PARAMETERS

@app.get("/products")
async def products(search: 
  Annotated[str, Query(max_length=10)] ):
  
  if search:
    serach_lower = search.lower()
    filtered_product = []
    for product in PRODUCTS:
      if serach_lower in product["product_name"].lower():
        filtered_product.append(product)
       
    return filtered_product
  return PRODUCTS   