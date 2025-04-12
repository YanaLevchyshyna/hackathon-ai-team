from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image
import io

app = Flask(__name__)
# classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

classifier = pipeline("image-classification")


@app.route("/predict-nsfw", methods=["POST"])
def predict_nsfw():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    try:
        file = request.files["file"]
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        predictions = classifier(image)
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
