# hackathon-ai-team
# **AI-API-SERVICES for the Hackathon**

This project provides a Flask-based API for image validation, NSFW content detection, and accessibility object detection. It is designed to integrate with external services, websites, mobile applications and Telegram bots.

---

## **Features**
- **NSFW Content Detection**: Validates images to determine if they contain inappropriate content.
- **Accessibility Object Detection**: Identifies accessibility-related objects (e.g., wheelchairs, ramps) in images using a CLIP model.
- **Cross-Origin Resource Sharing (CORS)**: Configured to allow secure communication with external services.
- **Logging**: Built-in logging for debugging and monitoring.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- Pipenv or virtualenv for managing dependencies
- Pre-trained models for NSFW classification and object detection:
  - **NSFW Model**: Hugging Face model for image classification.
  - **CLIP Model**: Hugging Face CLIP model for object detection.

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/hackathon-ai-team.git
   cd hackathon-ai-team

   2. Set Up a Virtual Environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   3. Install Dependencies
   pip install -r requirements.txt

   4. Set Up Configuration

   Create a .env file in the root directory.
   Add the following environment variables

   5. Run the Application
   flask run

#### API Endpoints ####
1. Home Route
Endpoint: /
Method: GET
Description: Health check endpoint to verify the service is running.
2. Version Route
Endpoint: /version
Method: GET
Description: Returns the current version of the API.
3. Test UI Route
Endpoint: /test_ui
Methods: GET, POST
Description: Renders the index.html template for testing the UI.
4. Check Image Route
Endpoint: /check_img
Method: POST
Description: Validates an image and checks for NSFW content.
Request Body
{
  "filename": "string"
}
Response:
{
  "response": "boolean"
}
5. Upload Image Route
Endpoint: /upload_img
Method: POST
Description: Detects accessibility-related objects in an image and upload an image to the temp folder/DB
Response:
{
  "response": [
    {
      "label": "string",
      "probability": "float"
    }
  ]
}

#### Project structure #####
hackathon-ai-team/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── accessibility_checker.py
│   │   ├── nsfw_filter.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_handler.py
│   │   ├── file_validator.py
│   ├── __init__.py
│
├── static/
│   ├── temp/
│
├── templates/
│   ├── index.html
│
├── config/
│   ├── base.py
│   ├── dev.py
│   ├── prod.py
│
├── .env
├── requirements.txt
├── README.md
├── run.py

###### Logging  #######
The application uses Python's built-in logging module. Logs are displayed in the following format:

Contributing 
Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your fork.
Submit a pull request.
License


Contact
For questions or support, please contact the project team at .
