import gradio as gr
import pytesseract
from PIL import Image

# Define OCR function
def perform_ocr(image, keyword):
    # Load image using PIL
    img = Image.open(image)
    
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(img, lang='eng+hin')
    
    # Search for the keyword in the OCR result
    if keyword.lower() in text.lower():
        return f"Keyword '{keyword}' found in the text!"
    else:
        return "Keyword not found in the text."

# Define Gradio interface
iface = gr.Interface(
    fn=perform_ocr,
    inputs=[gr.Image(type="filepath"), gr.Textbox(label="Search Keyword")],
    outputs="text",
    title="OCR and Document Search",
    description="Upload an image and enter a keyword to search in the extracted text."
)

# Launch the interface
iface.launch()
