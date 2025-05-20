import google.genai as genai
from django.conf import settings

client = genai.Client(api_key=settings.GENAI_API_KEY)

def generate_response(prompt):
    model = client.Model(
        model="google/flan-t5-xxl",
        temperature=0.7,
        max_output_tokens=256,
        top_p=0.95,
        top_k=40,
    )
    response = model.generate(prompt)
    return response.text

def clean_message(text):
    """Clean and preprocess incoming messages."""
    return text.strip().lower()