
from flask import current_app

def validate_image_extansion(file_name):

    if '.' not in file_name:
        return False, "No file extension found."
    
    ext = file_name.rsplit('.', 1)[1].lower()

    if ext not in current_app.config['ALLOWED_EXTENSIONS']:
        return False, f"Invalid file extension. Allowed extensions are: {', '.join(current_app.config['ALLOWED_EXTENSIONS'])}"

    return True, "No error, valid image file."



