import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

model = "gemini-2.0-flash-001"
content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
        model = model, contents = content
        )

print(response.text)

promt_token_count = response.usage_metadata.prompt_token_count
candidate_token_count = response.usage_metadata.candidates_token_count

print(f"Prompt tokens: {promt_token_count}")
print(f"Response tokens: {candidate_token_count}")
