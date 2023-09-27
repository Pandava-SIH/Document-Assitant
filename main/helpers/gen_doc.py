import time
import g4f
from util import split_text_into_chunks
import re

context = []

def get_summary(data_chunks: list[str]) -> str:
    """Generate initial summary """
    message = [{"role": "user", "content": text} for text in data_chunks]
    # message.append({"role":"user", "content":"summerize this document"})
    # chat completion method
    t = time.time()
    summary =  g4f.ChatCompletion.create(
        model= g4f.models.gpt_35_turbo,
        provider= g4f.Provider.You, #change model if required
        messages= message
    )
    return summary, time.time() - t


def chat_reponse(prompt: str):
    context.append({"role": "user", "content": prompt})
    # print(prompt)
    res = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        provider= g4f.Provider.You,
        messages=context
    )
    if res:
        context.append({"role": "system", "content": res})
    else:
        context.pop()
    print(res)


def generate_document(prompt: str):
    context.append({"role": "user", "content": prompt})
    
    res = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        provider= g4f.Provider.You,
        messages=context
        )
    context.append({"role":"system", "content": res})
    print(res)

if __name__ == "__main__":
    print(get_summary(split_text_into_chunks("""Hello !!""")))
    x = input()
    generate_document(x)

    while True :
        query = input()
        chat_reponse(query)


# def fill_legal_document(user_document_text, user_details, legal_document_template):
#     """
#     Fill in user details from their document into a legal document template.

#     Args:
#         user_document_text (str): Text extracted from the user's document.
#         user_details (dict): User-specific details to be filled into the legal document.
#         legal_document_template (str): Template of the legal document with placeholders.

#     Returns:
#         str: The filled legal document.
#     """

#     # Define regular expressions to identify placeholders in the template.
#     placeholder_pattern = r'\{[(\w+)]\}'  # Placeholder format: {placeholder_name}

#     # Find all placeholders in the template.
#     placeholders = re.findall(placeholder_pattern, legal_document_template)

#     # Initialize the filled document with the template.
#     filled_document = legal_document_template

#     # Iterate through placeholders and fill in user details.
#     for placeholder in placeholders:
#         if placeholder in user_details:
#             # Replace the placeholder with the corresponding user detail.
#             filled_document = filled_document.replace(f'{{{placeholder}}}', user_details[placeholder])
#         else:
#             print(f"Warning: Placeholder '{placeholder}' not found in user details.")

#     return filled_document