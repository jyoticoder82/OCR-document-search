# OCR and Document Search Web Application

This web application performs Optical Character Recognition (OCR) on images containing Hindi and English text and allows users to search for specific keywords within the extracted text. The application uses Python libraries such as **pytesseract** for OCR processing and **Gradio** for creating a user-friendly web interface.

## Features
- **Image Upload**: Upload an image with text in Hindi, English, or both.
- **OCR Processing**: Automatically extract text from the image using `pytesseract`.
- **Search Functionality**: Search for specific keywords within the extracted text.
- **Web Interface**: Simple and intuitive interface created with Gradio.
- **Supports Hindi and English**: Recognizes both Hindi and English text in images.

## Running Locally

To run the application locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/jyoticoder82/ocr-document-search.git
cd ocr-document-search

###2. Install Dependencies
Install the required Python libraries using pip:
pip install -r requirements.txt

###3. Run the Application
Run the web application with the following command:
python app.py

###![sample_image](https://github.com/user-attachments/assets/27b1cbe3-71a6-40af-92c8-ca1f2e966b5d)
This will launch the application locally, and you can access it in your browser at http://localhost:7860.
