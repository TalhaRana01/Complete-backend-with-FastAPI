from fastapi import FastAPI, status, Query, HTTPException, Path, Header
from typing import List, Optional, Annotated
from enum import Enum
from pydantic import BaseModel, AfterValidator

app = FastAPI()




#  Simple basic route
# @app.get("/")
# async def home():
#   return {"message" : "Talha Rana"}


# ------------------------------------------------------------------------------------------------------
## Path Parameters 
# ------------------------------------------------------------------------------------------------------

# Get Request 
## Read or fetch All data

# @app.get("/products")
# async def all_product():
#   return  {"message" : "All products list"}


# GET Request 
# Read single product by id

# @app.get("/products/{product_id}")
# async def product(product_id : int):
#   return  {"message":"Product", "product ID" : product_id}

##  with Pydantic validation

class Product(BaseModel):
  id : int
  name : str | None = None
  price : float
  stock : int
  

# POST Request

# Create a product and status code 201
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# # dict data as a request body
# async def create_product(new_product: dict):
#   return {"message" : "Product is created", "product" : new_product}


# Create a product with Pydantic BaseModel
# Pydantic data as a request body
# @app.post("/products", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: Product):
#   return {"message" : "Product is created", "product" : new_product}

# # Product update route
# @app.put("/products/{product_id}")
# async def update_product(new_update_product : Product | None = None , product_id: int | None = None ):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}


# # Product partial update route
# @app.patch("/products/{product_id}")
# async def partial_update_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}

# #  Product Delete route 
# @app.delete("/products/{product_id}")
# async def delete_product(new_update_product : Product, product_id: int):
#   return {"message" : "Product updated successfully", "product Id" : product_id, "product" : new_update_product}



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

# Output 
# http://127.0.0.1:8000/product/Electronic
# http://127.0.0.1:8000/product/Clothing

# Practie with Prefined Value with Enum

# class Tech(str, Enum):
#   python = "Python"
#   javascript = "JavaScript"
#   java = "Java"

# @app.get("/course/{course}")
# async def get_product(course : Tech):
#   return {"response" : "Product Fetched", "category" : course}

# http://127.0.0.1:8000/course/Java
# http://127.0.0.1:8000/course/JavaScript
# http://127.0.0.1:8000/course/Python

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


# class Course(str, Enum):
#   python = "Python"
#   digital_marketing = "Digital-marketing"
#   freelancing = "Freelancing"
  
# @app.get("/course/{skill}")
# async def get_courses(skill: Course):
#   if skill == Course.python:
#     return {"message":"Suitable for you", "Course":  skill}
#   elif skill.value == Course.freelancing.value:
#     return {"message":"Suitable for you", "Course":  skill}
#   elif skill.value == "Digital-marketing":
#     return {"message":"Suitable for you", "Course":  skill}
#   else:
#     return {"message": "Unknow course"}
  


### ------------------------------------------------------------------------------------------------------
## CRUD Operation with dummy data
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



# Get all products
# @app.get("/products", status_code=status.HTTP_200_OK)
# async def all_products():
#   return {"message" : PRODUCTS}


# # Get Single Product
# @app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
# async def get_single_product(product_id : int):
#   for product in PRODUCTS:
#     if product['product_id'] == product_id:
#       return {"product": product}
#   raise HTTPException(status_code=404, detail="product not found")

# # Create product  
# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: dict):
#   PRODUCTS.append(new_product)
#   return {"response" : "Product created ", "new_product": new_product}

# # Update product
# @app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
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

# @app.get("/products")
# async def product(search:str):
#   return {"status" : "OK", "lan" : search}

# @app.get("/product")
# async def product(en:str):
#   return {"status" : "OK", "lan" : en}

# @app.get("/product")
# async def product(q:str):
#   return {"status" : "OK", "lan" : q}

# @app.get("/products")
# def get_search(search : str):
#   return search
# # print(get_search())


  
#  Password parameter is optional in query parameter 
# @app.get("/user")
# async def user_created(name: str, username: str, email: str, password: str | None = None):
#   return {"message" : "Account created", "your_name": name, "username":username, "your_email": email, "password": password }

# Validate Password Query 
# @app.get("/user")
# async def user_created(name: str, username: str, email: str, password: Annotated[str, Query(max_length=10)]):
#   return {"message" : "Account created", "your_name": name, "username":username, "your_email": email, "password": password }



# @app.get("/course")
# async def course(course: str, age: int, email:str, phone: str):
#   return {"course" : f"{course, age, email, phone}"}


### ------------------------------------------------------------------------------------------------------
## Multi Query Parameters
### ------------------------------------------------------------------------------------------------------

# @app.get("/product")
# async def product(q:str, limit: int, en:str):
#   return {"status" : "OK", "query" : q, "limit": limit, "language" : en}



# @app.get("/course")
# async def course(course: str, type: bool = True):
#   return {"course" : course, "type": type}

# student asked qeury : skill , name, age, email, seats

# skill required
#  name required
# age required
#  email optional
# seat  default value 10
# @app.get("/student/{student_id}")
# async def student_query(student_id: int, skill:str, name:str, age:int, email: str | None = None , seats: int = 20):
#   return {"student_id": student_id, "skill": skill, "name": name, "age": age, "email": email, "seats": seats}

# http://127.0.0.1:8000/student/1?skill=python&name=talharana&age=30


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
# All fields are required 
# @app.get("/product/{product_id}")
# async def product(product_id: int, category : str, limit: int) :
#   return {"status": "OK", "category" : category, "product_id" : product_id, "limit": limit}

# http://127.0.0.1:8000/product/01?category=tech&limit=5

# @app.get("/product/{product_id}")
# async def product(product_id: str, category : str | None = None, limit: int = 10) :
#   return {"status": "OK", "category" : category, "product_id" : product_id, "limit": limit}


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
#   """ aik optional query parameter hai. Agar user ?search=... send kare to search us value ko rakhay ga, warna None hoga. """
#   if search:
#     # search query ko small letter main convert kry ga
#     search_lower = search.lower()
#     # empty filtered_product list 
#     filtered_product = []
#     for product in PRODUCTS:
#       if search_lower in product["product_name"].lower():
#         # jo product filted ky bad es main add hon ge
#         filtered_product.append(product)
#     # Agr filtered product ha to usko dy ga 
#     return filtered_product
#   # wrna all products de ga
#   return PRODUCTS    



# Import Query from FastAPI for this code 

# Es code sy hum user query ko limit kr skty hain es method sy Query(default=None, max_length=5) old way to limit the query

# # Validation without Annotated
# @app.get("/products")
# async def products(search:str | None = Query(default=None, max_length=5, description="Search keyword for filtering products")):
#   if search:
#     search_lower = search.lower()
#     filtered_product = []
#     for product in PRODUCTS:
#       if search_lower in product["product_name"].lower():
#         filtered_product.append(product)
       
#     return filtered_product
#   return PRODUCTS    



# Annotated method import krain ge typing module sy
# Validation with Annotated

# @app.get("/products")
# async def products(search: Annotated[str | None, Query(max_length=10) ] = None):
  
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
# async def get_products(search : Annotated[list[str] | None, Query(description="Search your query", max_length=10)] = None):
  
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
# async def get_products(search: Annotated[list[str] | None, Query(alias="q" ,description="Search your query here.")] = None):
  
#   print("Query received:", search)
#   if search:
#     filtered_product = []
#     for product in PRODUCTS:
#         for s in search:
#            if s.lower() in product["product_name"].lower():
#               filtered_product.append(product)
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

# from fastapi import HTTPException

# @app.get("/products/{id}")
# async def get_product(id: int):
#     for product in PRODUCTS:
#         if product["product_id"] == id:
#             return product
#     raise HTTPException(status_code=404, detail="Product ID not found")



## Numeric Validation must be non-zero or non-negative
# @app.get("/products/{id}")
# async def get_product(id: Annotated[int | None, Path(gt=0)]):
#   for product in PRODUCTS:
#     if product["product_id"] == id:
#       return product
#   # return {"error":"Product not found"}
#   raise HTTPException(status_code=422, detail="Product ID not found")


# Add Metadata with Path

# @app.get("/products/{id}")
# async def get_product(id: Annotated[int, Path(gt=0, title="Product ID", description="Enter your Product ID", example="prod-")]):
#   for product in PRODUCTS:
#     if product["product_id"] == id:
#       return product
#   # return {"error":"Product not found"}
#   raise HTTPException(status_code=404, detail="Product ID not found")



# Combine both Path and Query Parameters  basic 



# @app.get("/products/{product_id}")
# async def get_product(product_id: int, review: bool = False, rating: float = None):
#     """
#     - product_id -> Path parameter
#     - review, rating -> Query parameters
#     Example:
#       /products/10?review=true&rating=5
#       http://127.0.0.1:8000/products/1?review=true&rating=4.5
#     """
#     return {
#         "product_id": product_id,
#         "show_review": review,
#         "rating_filter": rating
#     }


# Combining Path and Query Parameters 
# import  Query and Path parameter
    
@app.get("/products/{id}")
async def get_product(
  # Path numeric id Validation
  id : Annotated[int  | None , Path(gt=0, le=100, description="Enter your Product ID")], 
  # Query search product name validation
  search: Annotated[str | None, Query(alias="q", max_length=20, description="Search your product ")] = None):
  
  # id : Annotated[int , Path(gt=0, le=100)], search: Annotated[str | None, Query(alias="q", max_length=20)] = None)
  #  product ki 1 or search query match honi chahye 
  for product in PRODUCTS:
    if product["product_id"] == id:
      if search and search.lower() not in product["product_name"].lower():
        return {"error": "Product does not match search term."}
      return product
  raise HTTPException(status_code=404, detail="Product not found")

# http://127.0.0.1:8000/products/1?q=turbo
# http://127.0.0.1:8000/products/2?q=cream
      




  
  




          





