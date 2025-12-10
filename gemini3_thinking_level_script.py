import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Add 'gemini3-pro-preview' as the model
response = client.models.generate_content(
	model = 'gemini-3-pro-preview',
	contents = 'How does AI work?',
	config = GenerateContentConfig(
		thinking_config = types.ThinkingConfig(thinking_level = "low")
	),
)

print(response.text)
