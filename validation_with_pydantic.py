from fastapi import FastAPI
from typing import Dict, Annotated
from pydantic import BaseModel


app = FastAPI(title= "Talha Rana Professional AI Engineer ")


# PRODUCTS = [
#   {
#     "product_id": 1,
#     "product_name": "Turbo-Clean All-in-One Detergent",
#     "category": "Household Goods",
#     "price": 19.99,
#     "in_stock": True,
#     "description": "The revolutionary cleaner that promises to remove any stain instantly. Contains 'secret formula X.' (Warning: May leave a sticky residue.)"
#   },
#   {
#     "product_id": 2,
#     "product_name": "Eternal Youth Face Cream",
#     "category": "Cosmetics",
#     "price": 89.50,
#     "in_stock": False,
#     "description": "Instantly reduces the appearance of wrinkles by 100%. Side effects may include temporary, minor itching. Sold as a novelty item."
#   },
#   {
#     "product_id": 3,
#     "product_name": "Ultra-Power USB-C Cable (10ft)",
#     "category": "Electronics",
#     "price": 5.99,
#     "in_stock": True,
#     "description": "Guaranteed to charge your device 50% faster. Known to fail after three uses."
#   },
#   {
#     "product_id": 4,
#     "product_name": "Organic Gluten-Free Water",
#     "category": "Food & Drink",
#     "price": 3.49,
#     "in_stock": True,
#     "description": "The purest, most natural water, now with a 'certified organic' sticker. Tastes exactly like regular tap water."
#   },
#   {
#     "product_id": 5,
#     "product_name": "Invisible Wireless Headphones",
#     "category": "Electronics",
#     "price": 199.00,
#     "in_stock": False,
#     "description": "So small and seamless, you won't even know you're wearing them! (Because they're literally just an empty box.)"
#   }
# ]

class Product(BaseModel):
  id : int
  name : str
  price : float
  stock : int | None = None
  
  
# Get all products
# @app.get("/products")
# async def get_products():
#   return PRODUCTS


# withouy Pydantic 
# create a product
# @app.post("/products")
# async def create_product(new_product : Product):
#   return new_product 


# Accessing Product attribute in function
@app.post("/products")
async def create_product(new_product : Product):
  """Es sy hum pydantic class model main to attribute ya variables hain unko access kr skty hain"""
  print(new_product.id)
  print(new_product.name)
  print(new_product.price)
  print(new_product.stock)
  return new_product 
  