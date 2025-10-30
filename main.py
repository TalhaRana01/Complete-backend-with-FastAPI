from fastapi import FastAPI, status, Query, HTTPException, Path
from typing import List, Optional, Annotated
from enum import Enum
from pydantic import BaseModel, AfterValidator

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
#   return  {"message":"Product", "product ID" : product_id}

## Pydantic 

class Product(BaseModel):
  name : str | None = None
  price : float
  

# POST Request

# Create a product
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: dict):
#   return {"message" : "Product is created", "product" : new_product}


# Create a product with Pydantic BaseModel

# @app.post("/product")
# async def create_product(new_product: Product):
#   return {"message" : "Product is created", "product" : new_product}


# @app.put("/product/{product_id}")
# async def update_product(new_update_product : Product | None = None , product_id: int | None = None ):
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

# # # Get all products
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
# def get_single_product(product_id: int):
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

# # Create product  
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


  

# @app.get("/user")
# async def user_created(name: str, username: str, email: str, password: Annotated[str, Query(max_length=10)]):
#   return {"message" : "Account created", "your_name": name, "username":username, "your_email": email, "password": password }



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


##----------------------------------------------------------------------------------------
## User Crud 
##----------------------------------------------------------------------------------------



# # Initialize app
# app = FastAPI(title="User CRUD API")

# # Pydantic model for user data
# class User(BaseModel):
#     id: int | None = None
#     name: str
#     email: str
#     age: Optional[int] = None

# # Mock database (in-memory list)
# users_db: List[User] = []

# # CREATE user
# @app.post("/users", response_model=User)
# async def create_user(user: User):
#     # Check if email already exists
#     for u in users_db:
#         if u.email == user.email:
#             raise HTTPException(status_code=400, detail="Email already exists")

#     users_db.append(user)
#     return user

# # READ all users
# @app.get("/users", response_model=List[User])
# async def get_users():
#     return users_db

# # READ single user by ID
# @app.get("/users/{user_id}", response_model=User)
# async def get_user(user_id: int):
#     for user in users_db:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")

# # UPDATE user
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, updated_user: User):
#     for index, user in enumerate(users_db):
#         if user.id == user_id:
#             users_db[index] = updated_user
#             return updated_user
#     raise HTTPException(status_code=404, detail="User not found")

# # DELETE user
# @app.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     for index, user in enumerate(users_db):
#         if user.id == user_id:
#             users_db.pop(index)
#             return {"message": "User deleted successfully"}
#     raise HTTPException(status_code=404, detail="User not found")




### ------------------------------------------------------------------------------------------------------
## Basic Query Parameters
### ------------------------------------------------------------------------------------------------------

PRODUCTS = [
  {
    "product_id": 1,
    "product_name": "Turbo-Clean All-in-One Detergent",
    "category": "Household Goods",
    "price": 19.99,
    "in_stock": True,
    "description": "The revolutionary cleaner that promises to remove any stain instantly. Contains 'secret formula X.' (Warning: May leave a sticky residue.)"
  },
  {
    "product_id": 2,
    "product_name": "Eternal Youth Face Cream",
    "category": "Cosmetics",
    "price": 89.50,
    "in_stock": False,
    "description": "Instantly reduces the appearance of wrinkles by 100%. Side effects may include temporary, minor itching. Sold as a novelty item."
  },
  {
    "product_id": 3,
    "product_name": "Ultra-Power USB-C Cable (10ft)",
    "category": "Electronics",
    "price": 5.99,
    "in_stock": True,
    "description": "Guaranteed to charge your device 50% faster. Known to fail after three uses."
  },
  {
    "product_id": 4,
    "product_name": "Organic Gluten-Free Water",
    "category": "Food & Drink",
    "price": 3.49,
    "in_stock": True,
    "description": "The purest, most natural water, now with a 'certified organic' sticker. Tastes exactly like regular tap water."
  },
  {
    "product_id": 5,
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

# @app.get("/products")
# async def products(search: 
#   Annotated[str, Query(max_length=10)] ):
  
#   if search:
#     serach_lower = search.lower()
#     filtered_product = []
#     for product in PRODUCTS:
#       if serach_lower in product["product_name"].lower():
#         filtered_product.append(product)
       
#     return filtered_product
#   return PRODUCTS   


#  Multiple Search Terms ( List)

# @app.get("/products")
# async def get_products(search : Annotated[list[str] | None, Query()] = None):
  
#   if search:
#     filtered_product = []
#     for product in PRODUCTS:
#       for s in search:
#         if s.lower() in product["product_name"].lower():
#           filtered_product.append(product)
#     return filtered_product
#   return PRODUCTS




# Alias parameters Query(alias="q")

# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(alias="q")] = None):
  
#   if search:
#     filtered_product = []
#     for product in PRODUCTS:
#       for s in search:
#         if s.lower() in product["product_name"].lower():
#           filtered_product.append(product)
#     return filtered_product
#   return PRODUCTS

# Adding Metadata
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(alias="q", title="Search Products", description="Search by product title",deprecated=True )] = None):
  
#   if search:
#     filtered_product = []
#     for product in PRODUCTS:
#       for s in search:
#         if s.lower() in product["product_name"].lower():
#           filtered_product.append(product)
#     return filtered_product
#   return PRODUCTS


# Custom Validation 
#  import  AfterValidator from Pydantic Model
# def check_valid_id(id : str):
#   """agr koi product id search nhi krta ha 
#       dash ky sath
#   """
#   if not id.startswith("prod-"):
#     # to ya error den ge
#     raise ValueError("ID must be start with 'prod-")
#   return id

# @app.get("/products")
# async def get_products(id: Annotated[str | None,AfterValidator(check_valid_id) ] = None):
#   """Es function main hum ny check_valid_id function ko call kia ha AfterValidator main"""
  
#   if id:
#     return {"id": id, "message": "Valid product ID"}
#   return {"message": "No ID provided"}



### ------------------------------------------------------------------------------------------------------
## Path Parameters and Numeric Validations
### ------------------------------------------------------------------------------------------------------

#  Basic Path Parameter

# @app.get("/products/{id}")
# async def get_product(id: int):
#   for product in PRODUCTS:
#     if product["product_id"] == id:
#       return product
#   # return {"error":"Product not found"}
#     raise HTTPException(status_code=404, detail="Product ID not found")


# Numeric Validation
@app.get("/products/{id}")
async def get_product(id: Annotated[int, Path(gt=0, title="Product ID", description="Enter your Product ID", example="prod-")]):
  for product in PRODUCTS:
    if product["product_id"] == id:
      return product
  # return {"error":"Product not found"}
  raise HTTPException(status_code=404, detail="Product ID not found")
    




  
  




          





