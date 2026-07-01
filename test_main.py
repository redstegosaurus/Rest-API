from io import BytesIO
from fastapi.testclient import TestClient
from main import app  # This brings in your FastAPI app

# Create the Test Client
client = TestClient(app)

# Create fake file in memory
byteStr = b"GIF89a..."  
fake_file = BytesIO(byteStr)

# The Test Function
def test_resize_image():
    # Format: (filename, file_object, mime_type)
    file_data = ("test_image.gif", fake_file, "image/gif")
    
    # Send the POST request
    # 'files' expects a dict: { "field_name": tuple_data }
    response = client.post("/resize", files={"file": file_data})
    
    assert response.status_code == 200
    
    # Optional: Check if the response is actually an image
    assert response.headers["content-type"] == "image/gif"
