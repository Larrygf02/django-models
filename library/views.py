from django.shortcuts import render

# Create your views here.
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100,100, "Hello World")
    p.showPage()
    p.save()

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')