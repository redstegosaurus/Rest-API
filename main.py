import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import shutil

app = FastAPI()

# Configuration
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

# Make some directiories just in case
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Image Resizer API is running. Try POST /resize!"}

@app.post("/resize")
async def resize_image(
    file: UploadFile = File(...), 
    width: int = 800, 
    height: int = 600
):
    # Make sure that its a image
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        raise HTTPException(status_code=400, detail="Only image files are allowed")


    # Make a new file name to avoid any conflicts 
    original_ext = file.filename.split(".")[-1]
    unique_id = uuid.uuid4()
    upload_filename = f"{unique_id}.{original_ext}"
    output_filename = f"resized_{unique_id}.{original_ext}"

    upload_path = os.path.join(UPLOAD_DIR, upload_filename)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    try:
        # Save the file to disk
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

       # Open and resize with pillow
        with Image.open(upload_path) as img:
            # Handle transparency (RGBA) if saving as JPEG
            if img.mode in ("RGBA", "P") and original_ext.lower() in ("jpg", "jpeg"):
                img = img.convert("RGB")
            
            # Resize the image
            # Image.Resampling.LANCZOS is high-quality downsampling
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # Save the result
            resized_img.save(output_path)

        # Gives it back
        return FileResponse(
            path=output_path, 
            filename=output_filename, 
            media_type="image/jpeg" if original_ext.lower() in ("jpg", "jpeg") else "image/png"
        )

    except Exception as e:
        # Log the error (in a real app, use a logger)
        print(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    
    finally:
        # Delete the temporary uploaded file
        if os.path.exists(upload_path):
            os.remove(upload_path)

# Optional: Health check
@app.get("/health")
async def health():
    return {"status": "ok"}