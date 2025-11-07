# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse


# app = FastAPI()

# # fruits = {
# #   "apple": "A juicy fruit",
# #   "banana": "A yellow delight"
# #   }


# # create Exception  class

# # class FruitException(Exception):
# #   def __init__(self, fruit_name: str):
# #     self.fruit_name = fruit_name


# ## Custom Exception Handler

# # @app.exception_handler(FruitException)
# # async def fruit_expection_handler(request: Request, exc: FruitException):
# #   return JSONResponse(
# #     status_code=418,
# #     content={"message": f"{exc.fruit_name} is not valid"}
# #   )
  
# # @app.get("/fruits/{fruit_name}")
# # async def read_fruits(fruit_name: str):
# #     if fruit_name not in fruits:
# #       raise FruitException(fruit_name=fruit_name)
# #     return fruits[fruit_name]


# ## Override default expection handlers
# ## import RequestValidationError from fastapi.exceptions

# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse




# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc:RequestValidationError):
#   return PlainTextResponse(str(exc), status_code=400)
  
  
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#   return item_id