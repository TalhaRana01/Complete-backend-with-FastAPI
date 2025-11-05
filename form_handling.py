from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated


app = FastAPI(title="Form Handling")

## Simple HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def get_form():
  return """
    <html>
      <body>
        <h2>Login Form</h2>
        <form action="/login/" method= "post">
            <label for="username">username</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">password</label><br>
            <input type="password" id="password" name="password"><br>
            <input type="submit"  value="submit">
        </form>
      </body>
    </html>

"""
#  Login route with username and password validation
# @app.post("/login/")
# async def login(username : Annotated[str, Form(min_length=3)], password : Annotated[str, Form(min_length=3, max_length=20)]):
#   return {"username": username, "password": password}