import os
import logging
from flask import Flask
from flask_cors import CORS
from transformers import CLIPProcessor, CLIPModel, pipeline 

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,  
        format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )

def create_app(config_name):
    """
        Creates and configures the Flask application.
        This function initializes the Flask app with configurations, models init, extensions,
        and blueprints. 
        Returns:
            Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    config_module = f"config.{config_name}.DevConfig"
    app.config.from_object(config_module)
    CORS(app, resources={r"/*": {"origins": app.config['CORS_ORIGINS']}})

    setup_logging()

    app.clip_model =  CLIPModel.from_pretrained(app.config['DETECTION_MODEL'])
    app.clip_processor = CLIPProcessor.from_pretrained(app.config['DETECTION_MODEL'])

    app.nsfw_classifier = pipeline("image-classification", model=app.config['NSFW_MODEL'])
    app.upload_folder =  app.config['UPLOAD_FOLDER']
    app.file_path =  ''


    from app.api import main
    app.register_blueprint(main)

    return app