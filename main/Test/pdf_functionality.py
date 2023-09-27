import nltk
from nltk import sent_tokenize, word_tokenize
import fitz  # pip install PyMuPDF
import g4f

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

    while True :
        message = [{"role": "user", "content": text} for text in data_chunks]
        context.append(message)

        # chat completion method
        response = g4f.ChatCompletion.create(
            model= "gpt-3.5-turbo",
            provider= g4f.Provider.Bing,
            messages= context
        )

        print(response)
        
        # printing the model's reply
        reply = response.choices[0].message[{'content'}]
        print("Model:", reply)

        # adding the reply to context
        context.append({"role": "assistant", "content": reply})

        while True:
            # taking user input
            user_input = input("Query : ") 
            if user_input.lower() == "exit":
                break
        
        # interaction with user model
        get_summary(user_input)  



# main method 
if __name__ == "__main__":
    # pdf_text = read_pdf(r"C:\Users\hp\Downloads\U62 MTH302.pdf")
    pdf_text = """Title: The Significance and Evolution of the Constitution

Introduction

A constitution is the fundamental law of a nation, laying down the principles and rules by which a country is governed. It is the cornerstone upon which the entire legal framework of a nation is built. Constitutions come in various forms, ranging from written to unwritten, but they all serve a common purpose: to establish the framework for government, protect the rights and liberties of citizens, and define the relationship between the state and its people. This article explores the significance and evolution of constitutions in the context of modern nation-states.

The Significance of a Constitution

Rule of Law: A constitution enshrines the principle of the rule of law, which means that everyone, including the government itself, is subject to the law. This ensures that those in power are accountable for their actions and cannot act arbitrarily.

Protection of Rights: Constitutions typically include a bill of rights or a declaration of fundamental rights and freedoms. These provisions protect citizens' rights to free speech, religion, assembly, and other essential liberties, shielding them from government overreach.

Separation of Powers: Constitutions often establish a system of government with a separation of powers among the legislative, executive, and judicial branches. This division of authority prevents any one branch from becoming too powerful and helps maintain a system of checks and balances.

Stability and Governance: A constitution provides a stable framework for governance. It defines the structure of government, the roles of various institutions, and the procedures for decision-making, ensuring that the nation can function smoothly.

National Identity: Constitutions often contain elements that reflect a nation's history, culture, and values, helping to forge a sense of national identity and unity among citizens."""
    
    print(get_summary(split_text_into_chunks(pdf_text)))
