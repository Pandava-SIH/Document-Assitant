import nltk
from nltk import sent_tokenize

# Download NLTK data for sentence tokenization
#uncomment this to download tokenizer
nltk.download("punkt")

# for PDF handling
import PyPDF2

#Failing
def extract_text_from_pdf(pdf_path):
    text = ""  # Initialize an empty string to store the extracted text
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # Create a PDF reader object
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)  # Get a specific page from the PDF
                text += page.extractText()  # Extract text from the page and append to the text variable
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")  # Handle any exceptions
    return text  # Return the extracted text as a string


# Funtion for spliting a long text in smaller chunks




def split_text_into_chunks(text, chunk_size=500):
    sentences = sent_tokenize(text)  # Tokenize the text into sentences
    chunks = []  # Initialize an empty list to store the chunks
    current_chunk = ""  # Initialize an empty string for the current chunk

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence  # Add the sentence to the current chunk
        else:
            chunks.append(current_chunk.strip())  # Append the current chunk to the list of chunks
 
            current_chunk = sentence  

    # Append the last remaining chunk if not emty
    if current_chunk:
        chunks.append(current_chunk.strip())  

    return chunks 

