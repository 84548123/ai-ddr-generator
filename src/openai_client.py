import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_openai_api_key():
    api_key = (os.getenv("OPENAI_API_KEY") or "").strip().strip('"').strip("'")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add your OpenAI API key to the .env file."
        )

    if api_key.startswith("AIza"):
        raise RuntimeError(
            "OPENAI_API_KEY is set to a Google API key (starts with 'AIza'). "
            "Replace it with a real OpenAI API key from https://platform.openai.com/api-keys."
        )

    if not api_key.startswith("sk-"):
        raise RuntimeError(
            "OPENAI_API_KEY does not look like a valid OpenAI API key. "
            "Expected a key starting with 'sk-'."
        )

    return api_key


def get_openai_client():
    return OpenAI(api_key=get_openai_api_key())
