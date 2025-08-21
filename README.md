AI Background Remover 🖼️✨
A simple yet powerful web application to automatically remove the background from any image using AI. This project uses a Python FastAPI backend for the core processing and a clean HTML/CSS/JavaScript frontend for the user interface.

Features
AI-Powered: Utilizes the rembg library for highly accurate background removal.

Simple Interface: Clean, modern, and user-friendly drag-and-drop UI.

Side-by-Side Comparison: Instantly view the original and the processed image.

Easy to Use: No complex settings. Just upload an image and download the result.

Fast & Lightweight: Built with FastAPI for high-performance API serving.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8+

Git

⚙️ Setup and Installation
Follow these steps to get your project up and running on your local machine.

1. Clone the Repository
First, clone the project from GitHub to your local computer.

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

(Replace your-username and your-repository-name with your actual GitHub details)

2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to keep project dependencies isolated.

On Windows:

# Create the virtual environment
py -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

On macOS / Linux:

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

You will know it's active when you see (venv) at the beginning of your terminal prompt.

3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

🚀 Running the Application
To run the application, you need to start the backend server and then open the frontend file.

1. Start the Backend Server
With your virtual environment still active, run the following command in your terminal:

uvicorn main:app --reload

This will start the FastAPI server. You should see a message indicating it's running on http://127.0.0.1:8000. Keep this terminal window open.

2. Open the Frontend
Navigate to the project folder on your computer and open the index.html file in your favorite web browser (e.g., Chrome, Firefox, or Edge).

的使用方法 (How to Use)
Open index.html in your browser.

Drag and drop an image file onto the upload area, or click it to select a file from your computer.

Wait a few seconds for the processing to complete. You will see a loading spinner.

View the result in the side-by-side comparison.

Click the "Download Image" button to save the background-removed image (as a PNG file).

Click "Upload New" to process another image.

🛠️ Technology Stack
Backend: Python, FastAPI

Background Removal: rembg, onnxruntime

Frontend: HTML, CSS, JavaScript

Server: Uvicorn