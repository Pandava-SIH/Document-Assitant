# text_extraction using python and tesseract

import pytesseract
import requests
from PIL import Image
from io import BytesIO
from main.helpers import util
import json

def extract_text_from_image(image_path):
    try:
        # Load the image using PIL (Pillow)
        img = Image.open(image_path)

        # Perform OCR to extract text
        extracted_text = pytesseract.image_to_string(img)

        return extracted_text

    except Exception as e:
        print(f"Error extracting text from image: {str(e)}")
        return None

def make_http_request(url):
    try:
        # Send an HTTP GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            print(f"HTTP request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {str(e)}")
        return None
    




# Extract text from an image
image_path = 'images/test1.png'  # Replace with the path to your image file
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    print("Extracted Text:")
    # print(extracted_text)
    res = requests.post("http://127.0.0.1:8000/load_documents/", json={"documents": util.split_text_into_chunks(extracted_text)})
    print(res)
else:
    print("Text extraction failed.")

# Make an HTTP request
# url = 'https://example.com'  # Replace with the URL you want to request
# response_text = text_extraction.make_http_request(url)

# if response_text:
#     print("\nHTTP Response:")
#     print(response_text)
# else:
#     print("HTTP request failed.")
