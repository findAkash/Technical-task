from datetime import datetime
import io
import os
from typing import Annotated
from fastapi import APIRouter, File, UploadFile
import image_process
from config import Config
from PIL import Image

router = APIRouter()


@router.get("/")
def read_root():
    return {"Success": True, "Message": "The api is running!"}

@router.post("/segment-image")
async def segment_image(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):  
    start = datetime.now()
    print(f"start time: {start}")
    output_files = []
    os.makedirs(os.path.dirname(Config.OUTPUT_DIR), exist_ok=True)
    for file in files:
        output_path = Config.OUTPUT_DIR + file.filename.split('.')[0]+".png"
        
        file_contents = await file.read()
        image_data = io.BytesIO(file_contents)
        image = Image.open(image_data).convert("RGB")
        fig = image_process.segment_everything(image=image)
        # Save image as .png
        fig.save(output_path)

        print(f"total time: {datetime.now() - start}")
    
    return {"success": True, "outputs": output_files}