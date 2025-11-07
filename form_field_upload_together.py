from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil


app = FastAPI(title="Form Handling")

## Import Form from FastAPi
## import HTMLResponse from fastapi.responses
## Simple HTML form for testing
## simple render HTML form with response class
@app.get("/", response_class=HTMLResponse)
async def get_form():
  return """
    <html>
      <body>
        <h2>User form</h2>
        <form action="/user--with-file/" enctype="multipart/form-data" method= "post">
          <label for="username">Username</label><br>
           <input name="username" type="text" id="username" required>
           <input type="submit" value="Upload"><br><br>
          <label for="file">Profile Picture</label><br>
           <input name="file" type="file" id="file" accept="image/*">
           <input type="submit" value="Submit">
        </form>
       
      </body>
    </html>

"""

@app.post("/user--with-file/")
async def user_profile_upload(
  username: Annotated[str, Form() ],
  file: Annotated[UploadFile | None, File()] = None):
  
  response = {"username": username}
  if file:
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(save_path, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    response["filename"] = file.filename
  return response
      
  
  


# # save file in local system 
# @app.post("/files/")
# async def upload_file(file: Annotated[bytes | None, File() ] = None):
  
#   if not file:
#     return {"message": "Not file sent"}
#   filename = f"{uuid.uuid4()}.bin"
#   save_path = f"uploads/{filename}"
#   os.makedirs("uploads",exist_ok=True )
  
#   with open(save_path,"wb" ) as buffer:
#     buffer.write(file)
#   return {"file size" : len(file)}


# @app.post("/uploadfiles/")
# async def create_upload_file(files: Annotated[list[UploadFile], File()]):
#   save_files = []
#   os.makedirs("uploads", exist_ok=True)
#   for file in files:
#     save_path = f"uploads/{file.filename}"
#     with open(save_path, "wb") as buffer:
#       shutil.copyfileobj(file.file, buffer)
#     save_files.append({"filename": file.filename})
#   return save_files
    