# src/test_openai_key.py
from config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

def test_api_key():
    print(f"API Key: {OPENAI_API_KEY}")
    # Simple test to check API connection
    try:
        response = client.models.list()
        print("API connection successful. Models available:")
        for model in response.data:
            print(model['id'])
    except openai.OpenAIError as e:
        print(f"Error connecting to OpenAI API: {e}")

if __name__ == "__main__":
    test_api_key()
