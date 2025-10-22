import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)


with open("equipo.jpg", "rb") as f:
    image_bytes = f.read()


model = genai.GenerativeModel("gemini-pro-vision") 

response = model.generate_content([
    "¿Qué tipo de equipamiento médico se observa en esta imagen?",
    {
        "mime_type": "image/jpeg",
        "data": image_bytes
    }
])

print("=== Respuesta del modelo ===")
print(response.text)