import nltk
from nltk import sent_tokenize, word_tokenize
import fitz  # pip install PyMuPDF
import g4f
import pytesseract
import time 

# comment out for first time download
# nltk.download('punkt')


# to extract text from the pdf
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ''

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text

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

# to fetch summary out of the text we got
def get_summary(data_chunks: list[str]) -> str:
        context = []
        
        message = [{"role": "user", "content": text} for text in data_chunks]
        context.append(message)

        # chat completion method
        response = g4f.ChatCompletion.create(
        model= g4f.models.gpt_35_turbo,
        provider= g4f.Provider.Bing, #change model if required
        messages= message
        )

        print(response)

        while True:
            query = input()
            context.append({"role":"user", "content":query})
            response_q = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                provider = g4f.Provider.Bing,
                messages=context)
            print(response_q)
            context.append({"role":"system", "content":response_q})




    # message.append({"role":"user", "content":"summerize this document"})
    # chat completion method
    
    # context.append(response)
    # while True:
    #     query = input("You : ")
    #     message ({"role":"user", "content":query})
    #     response_q = g4f.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     provider = g4f.Provider.Aichat,
    #     messages=context)
    #     print(response_q)
    #     context.append({"role":"system", "content":response_q})

    # print(response)
        
    # # printing the model's reply
    # reply = response.choices[0].message[{'content'}]
    # print("Model:", reply)

    # # adding the reply to context
    # context.append({"role": "assistant", "content": reply})

    # while True:
    #     # taking user input
    #     user_input = input("Query : ") 
    #     if user_input.lower() == "exit":
    #         break
        
    # # interaction with user model
    # get_summary(user_input)  

# main method 
if __name__ == "__main__":
    pdf_text = read_pdf(r"C:\Users\hp\Downloads\Legal Agreement Form.pdf")
    # pdf_text = "Hello ! I am satyam gupta"
    print(get_summary(split_text_into_chunks(pdf_text)))
