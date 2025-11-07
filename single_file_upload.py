from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
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
        <h2>Single file Upload</h2>
        <form action="/files/" enctype="multipart/form-data" method= "post">
           <input name="file" type="file">
           <input type="submit" value="Upload">
        </form>
        <h2>Single file Upload(Uploadfiles)</h2>
        <form action="/uploadfiles/" enctype="multipart/form-data" method= "post">
           <input name="file" type="file">
           <input type="submit" value="Upload">
        </form>
      </body>
    </html>

"""
# file upload
@app.post("/files/")
async def upload_file(file: Annotated[bytes | None, File() ] = None):
  
  if not file:
    return {"message": "Not file sent"}
  return {"file size" : len(file)}


# save file in local system 
@app.post("/files/")
async def upload_file(file: Annotated[bytes | None, File() ] = None):
  
  if not file:
    return {"message": "Not file sent"}
  filename = f"{uuid.uuid4()}.bin"
  save_path = f"uploads/{filename}"
  os.makedirs("uploads",exist_ok=True )
  
  with open(save_path,"wb" ) as buffer:
    buffer.write(file)
  return {"file size" : len(file)}


@app.post("/uploadfiles/")
async def create_upload_file(file: Annotated[UploadFile | None , File()] = None):
  if not file:
    return {"message": "Not upload file sent"}
  
  save_path = f"uploads/{file.filename}"
  os.makedirs("uploads", exist_ok=True)
  with open(save_path, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)
  return {"filename" : file.filename, "content_type": file.content_type} 
    
    