import pytesseract
from PIL import Image
import json

# Function to extract text from image
def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')  # Supports Hindi and English
        
        # Optionally convert the text to a structured format (e.g., JSON)
        text_data = {
            "extracted_text": extracted_text
        }
        return json.dumps(text_data, indent=4)
    
    except Exception as e:
        return str(e)

# Example of usage
if __name__ == "__main__":
    image_path = "C:/Users/HIMANSHU GAUTAM/Desktop/sample_image.png"  
    result = extract_text_from_image(image_path)
    print(result)
