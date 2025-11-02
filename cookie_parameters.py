from fastapi import FastAPI, Cookie, Body
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
  
  
@app.get("/products/recommendations")
async def get_recommendations(cookie : Annotated[ProductCookie, Cookie()]):
  response = {"session_id" : cookie.session_id}
  if cookie.prefered_category:
    response["message"] = f"Recommendations for {cookie.prefered_category} products"
  else:
    response["message"] = f"Default recommedations for session {cookie.session_id}"
  if cookie.tracking_id:
    response["message"] = cookie.tracking_id
  return response

