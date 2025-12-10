import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Add 'gemini3-pro-preview' as the model
response = client.models.generate_content(
	model = 'gemini-3-pro-preview',
	contents = 'What is C++?'
)

print(response.text)
