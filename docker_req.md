🚀 **Deployment Request: NSFW Image Classification API (Flask + Hugging Face)**
📌 Goal
Deploy a Flask API that performs NSFW image classification using the Hugging Face model `Falconsai/nsfw_image_detection`. The model should be pre-downloaded inside a Docker image so that no internet access is required at runtime.


**📁 Expected API**
- Method: POST

- Endpoint: /predict-nsfw

- Request: multipart/form-data with a field named "file" (image)

- Response: JSON array of label + score, e.g.:


**⚙️ Tech Stack**
Python: 3.12

Framework: Flask

Dependencies: transformers, torch, pillow, flask



📦 Files to Include in Build
app.py

requirements.txt

Dockerfile


✅ Expected Outcome
The model is baked into the Docker image (no internet needed at runtime).

The container serves the image classification API on port 8000.

I can send images via POST and get NSFW prediction results.