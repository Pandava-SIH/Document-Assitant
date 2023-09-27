import nltk
from nltk import sent_tokenize
import fitz

# Download NLTK data for sentence tokenization
# uncomment this to download tokenizer for first time 
# nltk.download("punkt")

# to extract text from the pdf
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ''

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text

# Example usage:
# pdf_text = read_pdf(r"C:\Users\hp\Downloads\U62 MTH302.pdf")

# splits the entire text into equal chunks 
# then, store in a list & give to the llm 
def split_text_into_chunks(text, chunk_size=512):

    # Tokenize the entire text into sentences
    sentences = sent_tokenize(text) 

    # Initialize an empty list to store the chunks
    chunks = []  

    # Initialize an empty string for the current chunk
    current_chunk = ""  

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            # Add the sentence to the current chunk
            current_chunk += " " + sentence

        else:
            # Append the current chunk to the list of chunks
            chunks.append(current_chunk.strip()) 
            current_chunk = sentence  

    # Append the last remaining chunk if not emty
    if current_chunk:
        chunks.append(current_chunk.strip())  

    return chunks

