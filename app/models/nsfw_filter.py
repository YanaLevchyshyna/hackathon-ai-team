from PIL import Image
from transformers import pipeline

# Load the model only once when the module is imported
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

def is_safe_image(image_path, threshold=0.9):
    """
    Checks if an image is safe (i.e., not NSFW) using a pre-trained Hugging Face model.

    Args:
        image_path (str): Path to the image file.
        threshold (float): Probability above which the image is considered NSFW.

    Returns:
        bool: True if image is safe, False if it's flagged as NSFW.
    """
    image = Image.open(image_path).convert("RGB")
    results = classifier(image)

    for result in results:
        if result['label'].lower() == 'nsfw' and result['score'] > threshold:
            return False
    return True


# ---------------------  📦 Example usage:
# from nsfw_filter import is_safe_image

# print(is_safe_image("static/uploads/test_image2.jpg"))
# # Output: True or False
