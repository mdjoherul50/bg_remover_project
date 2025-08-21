from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import io

# Initialize the FastAPI app
app = FastAPI(title="Background Removal API")

# Add CORS middleware to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    """ A simple endpoint to check if the API is running. """
    return {"message": "Welcome to the Background Removal API!"}

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    """
    Receives an image file, removes its background,
    and returns the processed image.
    """
    # Read the image file content
    input_image_bytes = await file.read()
    
    # Use rembg to remove the background
    output_image_bytes = remove(input_image_bytes)
    
    # Return the processed image as a streaming response
    return StreamingResponse(io.BytesIO(output_image_bytes), media_type="image/png")