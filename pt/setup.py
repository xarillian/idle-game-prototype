import os

import openai
from dotenv import load_dotenv


def initialize_llm():
    """ TODO """
    # TODO docstring
    load_dotenv()
    client = openai.OpenAI()
    client.api_key = os.getenv('OPENAI_API_KEY')

    return client
