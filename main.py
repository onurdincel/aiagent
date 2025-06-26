import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

model = "gemini-2.0-flash-001"

if len(sys.argv) < 1:
    print("need one argument")
    sys.exit(1)

user_prompt = sys.argv[1]

messages = [
        types.Content(role = "user", parts=[types.Part(text=user_prompt)]),
    ]

response = client.models.generate_content(
        model = model, contents = messages
        )

print(response.text)

if "--verbose" in sys.argv:
    promt_token_count = response.usage_metadata.prompt_token_count
    candidate_token_count = response.usage_metadata.candidates_token_count
    
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {promt_token_count}")
    print(f"Response tokens: {candidate_token_count}")
