from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")


client = genai.Client(api_key=API_KEY)


stream = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents="Explica detalladamente cómo funciona el sistema respiratorio humano."
)


for chunk in stream:
    if chunk.text:
        print(chunk.text, end="", flush=True)
