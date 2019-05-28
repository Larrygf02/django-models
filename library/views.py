from django.shortcuts import render

# Create your views here.
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

def index(request):
    context = {
        'mensaje': 'Generar pdf'
    }
    return render(request, 'library/index.html', context)

def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100,100, "Hello World")
    p.showPage()
    p.save()

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def generate_csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hola.csv"'

    writer = csv.writer(response)
    writer.writerow(['Primera fila', 'Norma', 'Navarrete'])
    writer.writerow(['Segunda fila', 'A', 'B'])

    return response