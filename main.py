import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

try:
    query = sys.argv[1]
    joined_query = "".join(query)
    assert joined_query != ""
except (IndexError, AssertionError):
    sys.stderr.write("Please enter a prompt.\n")
    sys.exit(1)

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=joined_query)])
    ]

response = client.models.generate_content(
    model="gemini-2.0-flash-001", 
    contents=messages
    )
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count
print(response.text)

if "--verbose" in sys.argv:
    print(f"User prompt: {joined_query}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")