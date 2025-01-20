from groq import Groq
from dotenv import load_dotenv
import os


def draft_message(content, role='user'):
    return {
        "role": role,
        "content": content
    }



def AISum(link):
    load_dotenv()
    api_key = os.getenv('api_key')

    linker = link
    client = Groq(api_key=api_key)

    messages = [
        {
            'role': 'system',
            'content': "You are an article summarizer that gives clear and concise summaries on artciesl given to you via link, and you always start with The article talks about "
        }
    ]
    prompt = f'Can you give a synopsis of the article in this link? {linker}'
    messages.append(draft_message(prompt))

    chat_completion = client.chat.completions.create (
    temperature = 1.0,
    n = 1,
    model = "mixtral-8x7b-32768",
    max_tokens= 10000,
    messages=messages
)

    return chat_completion.choices[0].message.content

