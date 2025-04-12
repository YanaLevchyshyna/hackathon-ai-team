from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# Load model and processor once (outside the function to avoid reloading)
model_name = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_name)
processor = CLIPProcessor.from_pretrained(model_name)

# Define the descriptions for accessibility comparison
ACCESSIBILITY_LABELS_EN = [
    "a photo of a wheelchair ramp",
    "a photo of a Braille sign",
    "a photo of tactile paving",
    "a photo of a call button for assistance",
    "a photo of parking spots for people with disabilities",
    "a photo of wide doors for wheelchair access",
    "nothing related to accessibility"
]

def check_accessibility_objects(image_path, labels=ACCESSIBILITY_LABELS_EN):
    """
    Compare an image with text descriptions of accessibility-related objects using CLIP.

    Args:
        image_path (str): Path to the image file.
        labels (list of str): Descriptions to compare against.

    Returns:
        list of dict: Each item contains 'label' and 'probability' keys.
    """
    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    # Compute similarity
    with torch.no_grad():
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)[0]

    # Return label-probability pairs
    return [{"label": label, "probability": round(prob.item(), 4)} for label, prob in zip(labels, probs)]



# ----------------------  Example usage:
# from clip_accessibility_checker import check_accessibility_objects

# image_path = "static/uploads/test_image.jpg"
# results = check_accessibility_objects(image_path)

# for res in results:
#     print(f"{res['label']}: {res['probability']*100:.2f}%")
