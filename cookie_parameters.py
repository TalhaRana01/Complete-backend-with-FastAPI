from fastapi import FastAPI, Cookie, Body, Header
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()


# ------------------------------------
# Cookie Parameters
# ------------------------------------

# @app.get("/products/recommendations/")  # ✅ fixed (added leading slash)
# async def get_recommendations(
#     session_id: Annotated[str | None, Cookie()] = None
# ):
#     if session_id:
#         return {
#             "message": f"Recommendations for session {session_id}",
#             "session_id": session_id
#         }
#     return {"message": "No session ID provided — showing default recommendations"}




# ------------------------------------
# Muitiple Cookie Parameters
# ------------------------------------

class ProductCookie(BaseModel):
  session_id: str
  prefered_category : str | None = None
  tracking_id : str | None = None
  
  
# @app.get("/products/recommendations")
# async def get_recommendations(cookies : Annotated[ProductCookie, Cookie()]):
#   response = {"session_id" : cookies.session_id}
  
#   if cookies.prefered_category:
#     response["message"] = f"Recommendations for {cookies.prefered_category} products"
#   else:
#     response["message"] = f"Default recommedations for session {cookies.session_id}"
#   if cookies.tracking_id:
#     response["traacking_id"] = cookies.tracking_id
#   return response

# -----------------------------
# Forbidding Extra Cookies
# -----------------------------


# class ProductCookie(BaseModel):
#   model_config = {"extra": "forbid"}
#   session_id: str
#   prefered_category : str | None = None
#   tracking_id : str | None = None
  
  
# @app.get("/products/recommendations")
# async def get_recommendations(cookies : Annotated[ProductCookie, Cookie()]):
#   response = {"session_id" : cookies.session_id}
  
#   if cookies.prefered_category:
#     response["message"] = f"Recommendations for {cookies.prefered_category} products"
#   else:
#     response["message"] = f"Default recommedations for session {cookies.session_id}"
#   if cookies.tracking_id:
#     response["traacking_id"] = cookies.tracking_id
#   return response

# -----------------------------
# Combining with body Parameters
# -----------------------------

class ProductCookie(BaseModel):
  model_config = {"extra": "forbid"}
  session_id: str = Field(title="Session ID", description="User session Identifier")
  prefered_category : str | None = Field(title="Prefered Category", description="User's prefered product category")
  tracking_id : str | None = None
  
  
class PriceFilter(BaseModel):
  min_price : float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
  max_price : float | None  = Field(default=None, title="Miximum Price", description="Miximum price for recommendations")
  
  
@app.post("/products/recommendations")
async def get_recommendations(
  cookies : Annotated[ProductCookie,
  Cookie()], 
  price_filter: Annotated[PriceFilter, Body(embed=True)] ):
  
  response = {"session_id" : cookies.session_id}
  
  if cookies.prefered_category:
    response["category"] = cookies.prefered_category
  response["price_range"] = {
      "min_price": price_filter.min_price,
      "max_price" : price_filter.max_price
    }
  
  return response

# curl -X POST -H "Content-Type: application/json" -H "Cookie: session_id=abc123; prefered_category=tech; tracking_id=xyz123" -d {\"price_filter\": {\"min_price\": 1000, \"max_price\": 5000}}" http://127.0.0.1:8000/products/recommendations
# curl -X POST -H "Content-Type: application/json" -H "Cookie: session_id=abc123; prefered_category=tech; tracking_id=xyz123" -d "{\"price_filter\": {\"min_price\": 1000, \"max_price\": 5000}}" http://127.0.0.1:8000/products/recommendations


# class ProductCookie(BaseModel):
#   session_id : str
#   prefered_category : str | None = None
#   tracking_id : str | None = None
  

# @app.get("/products/recommendations")
# async def get_recommendation(cookies: Annotated[ProductCookie, Cookie()]):
#   response = {"seesion_id" : cookies.session_id}
#   if cookies.prefered_category:
#     response["message"] = f"Recommendations for {cookies.prefered_category} products"
#   else:
#     response["message"] = f"Default recommendations for session {cookies.session_id}"
    
#   if cookies.tracking_id:
#     response["tracking_id"] = cookies.tracking_id
#   return response


# curl -H "Cookie: session_id=abc123; prefered_category=tech; tracking_id=xyz123" http://127.0.0.1:8000/products/recommendations


# @app.get("/products")
# async def get_products(user_agent: Annotated[str | None, Header() ] = None):
#   return {"user_agent": user_agent}

# Handling Duplicates Headers
@app.get("/products")
async def get_products(x_product_token: Annotated[list[str] | None, Header() ] = None):
  return {"x_product_token": x_product_token or []}