# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {
#   "apple": "A juicy fruit",
#   "banana": "A yellow delight"
#   }

# # Import HTTPException from FastAPI
# # Using HTTPException

# ## Get All Items
# # @app.get("/items")
# # async def get_item():
# #   return items

# ## Get single item
# # @app.get("/items/{item_id}")
# # async def get_item(item_id: str):
# #   if item_id not in items:
# #     raise HTTPException(status_code=404, detail="Item not found")
# #   return items[item_id]


# ## Adding Custom Header
# @app.get("/items/{item_id}")
# async def get_item(item_id: str):
#   if item_id not in items:
#     raise HTTPException(status_code=404, detail="Item not found", headers={"x-error-type": "itemmissing"})
#   return items[item_id]