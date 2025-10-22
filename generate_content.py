from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")


client = genai.Client(api_key=API_KEY)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="¿Por qué es importante dormir bien?"
)

# Mostrar respuesta
print("=== Respuesta del modelo ===")
print(response.text)
