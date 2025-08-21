from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from PIL import Image, ImageOps
import io

# Initialize the FastAPI app
app = FastAPI(title="Background Removal API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """ A simple endpoint to check if the API is running. """
    return {"message": "Welcome to the Background Removal API!"}

@app.post("/remove-background/")
async def remove_background(
    file: UploadFile = File(...),
    bg_image: UploadFile = File(None),
    bg_color: str = Form(None),
    width: int = Form(None),
    height: int = Form(None),
    passport: bool = Form(False)
):
    """
    Receives an image, removes background, and optionally applies a background image/color and resizing.
    """
    input_image_bytes = await file.read()
    
    # Remove background to get a transparent PNG
    output_image_bytes = remove(input_image_bytes)
    
    processed_image = Image.open(io.BytesIO(output_image_bytes))

    # Handle passport photo preset
    if passport:
        bg_color = "#FFFFFF"  # Force white background for passport
        width = 600
        height = 600

    # Apply background image if provided
    if bg_image:
        background_bytes = await bg_image.read()
        background = Image.open(io.BytesIO(background_bytes)).convert("RGBA")
        
        # Resize background to match the processed image
        resized_background = background.resize(processed_image.size, Image.Resampling.LANCZOS)
        
        # Paste the foreground (with transparency mask) onto the new background
        resized_background.paste(processed_image, (0, 0), processed_image)
        processed_image = resized_background.convert("RGB") # Convert to RGB as it now has a background

    # Apply background color if no background image was used
    elif bg_color:
        background = Image.new("RGB", processed_image.size, bg_color)
        background.paste(processed_image, (0, 0), processed_image)
        processed_image = background
    
    # Handle resizing. ImageOps.fit crops the image to the exact dimensions
    if width and height:
        processed_image = ImageOps.fit(processed_image, (width, height), Image.Resampling.LANCZOS)

    # Save the final image to a new byte stream
    final_image_stream = io.BytesIO()
    # Save as PNG to maintain quality
    processed_image.save(final_image_stream, format="PNG")
    final_image_stream.seek(0)
    
    return StreamingResponse(final_image_stream, media_type="image/png")
