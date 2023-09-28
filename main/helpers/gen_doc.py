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

