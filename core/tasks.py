from celery import shared_task
from . services.utils import generate_response, clean_message

@shared_task
def process_message(message):
    cleaned_message = clean_message(message)
    response = generate_response(cleaned_message)
    return response