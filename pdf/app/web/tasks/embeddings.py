from celery import shared_task

from app.web.db.models import Pdf
from app.web.files import download
from app.chat import create_embeddings_for_pdf


@shared_task()    # This decorator makes the function a Celery task which runs in the background.
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf_id) as pdf_path:
        create_embeddings_for_pdf(pdf_id, pdf_path)
