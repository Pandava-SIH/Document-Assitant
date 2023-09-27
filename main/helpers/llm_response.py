import g4f
import main.helpers.util
import time

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


if __name__ == "__main__":
    print(get_summary(util.split_text_into_chunks("""""")))