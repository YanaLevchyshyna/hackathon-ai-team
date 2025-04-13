import os
from flask import render_template, jsonify, request, current_app

from app.api import main
from app.models.accessibility_checker import check_accessibility_objects
from app.models.nsfw_filter import is_safe_image
from app.utils.file_validator import validate_image
from app.utils.file_handler import get_file_path

#image_path = "static/temp/test_image2.jpg"


@main.route('/')
def home():
    return 'AI-API-SERVICES for Chernihiv hackathon'

@main.route('/version', methods=['GET'])
def version():
    return 'Current version of AI-API-SERVICES is - 1'

@main.route('/test_ui', methods=['GET', 'POST'])
def test_ui():
    return render_template("index.html")


@main.route('/check_img', methods=['POST'])
def check_image():

    data = request.get_json()
    is_valid, error = validate_image(data['filename'])

    if is_valid:
        image_path = get_file_path(current_app.upload_folder, data['filename'])
        current_app.file_path = image_path
        is_unsafe = is_safe_image(current_app.nsfw_classifier, image_path) 
    else:
        return False    

    return jsonify({"response": is_unsafe})   

@main.route('/upload_img', methods=['POST'])
def upload_image():

    results = check_accessibility_objects(current_app.clip_model, current_app.clip_processor, current_app.file_path)
    for res in results:
     print(f"{res['label']}: {res['probability']*100:.2f}%")

    return jsonify({"response": results})




