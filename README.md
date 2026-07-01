# 🖼️ FastAPI Image Resizer

A high-performance REST API built with **Python** and **FastAPI** that resizes images on the fly. This project demonstrates backend engineering skills including asynchronous request handling, file processing, automated testing, and containerization.

## ✨ Features

- **Dynamic Resizing:** Upload any image and specify custom width/height dimensions.
- **Smart Processing:** Automatically handles image formats (JPEG, PNG, GIF, WebP) and converts transparency (RGBA) to RGB for compatibility.
- **High Quality:** Uses the `Pillow` library with the `LANCZOS` resampling filter for crisp results.
- **Stateless & Clean:** Automatically deletes temporary files after processing to prevent disk bloat.
- **Containerized:** Runs in a Docker/Podman container for consistent deployment across any environment.
- **Tested:** Includes `pytest` integration tests to ensure reliability.

## 🛠️ Tech Stack

| Category      | Technology          |
|---------------|---------------------|
| **Language**  | Python 3.12         |
| **Framework** | FastAPI             |
| **Server**    | Uvicorn (ASGI)      |
| **Image Lib** | Pillow (PIL)        |
| **Testing**   | Pytest, HTTPX       |
| **DevOps**    | Docker / Podman     |
| **Docs**      | Swagger UI (Auto)   |

## 🚀 Quick Start

### Option 1: Run Locally (Virtual Environment)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/redstego/Rest-API.git
   cd Rest-API

2. Create and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependancies
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Run the server
    uvicorn main:app --reload --host 0.0.0.0 --port 8000

### Option 2: Run with Docker/Podman

1. Build the image
   docker build -t image-resizer-app .
   # Or if using Podman:
   podman build -t image-resizer-app .

2. Run the container
    docker run -p 8000:8000 image-resizer-app
    #  Or if using Podman:
    podman run -p 8000:8000 image-resizer-app

### Running Tests
   pytest -v

This suite includes a test that uploads a mock image and verifies the response status and content type.

📡 API Usage
Endpoint: POST /resize
Resizes an uploaded image to the specified dimensions.

Parameters:

file (multipart/form-data): The image file to upload (.jpg, .png, .gif, .webp).
width (int, optional): Target width (default: 800).
height (int, optional): Target height (default: 600).
Example curl Request:

bash

Copy
curl -X POST "http://localhost:8000/resize" \
     -F "file=@/path/to/your/image.jpg" \
     -F "width=400" \
     -F "height=300" \
     --output resized_output.jpg
Response:

Returns the resized image file directly.
Status 200 OK on success.
Status 400 Bad Request if the file is not an image.
Status 500 Internal Server Error if processing fails.
📂 Project Structure
text

Copy
.
├── main.py              # FastAPI application logic
├── test_main.py         # Pytest test suite
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request
