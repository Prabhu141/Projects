from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm
from pdf2docx import parse
#import PyPDF2
#import pytesseract
#from pdf2image import convert_from_path
import io

def index(request):
    return HttpResponse("Hello, world!")


def spdf(request):
    sdocuments = Document.objects.all()
    for obj in sdocuments:
        title = obj.description 
        baseurls = obj.document
    print(baseurls)
    print(title)
    filepath = './media/'+str(baseurls)
    print(filepath)
    pdf_file = filepath
    word_file = './media/docx/output.docx'
    parse(pdf_file, word_file, start=0, end=None)
    return render(request, 'searchpdf.html', { 'sdocuments': sdocuments })

def pdf_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('spdf')
    else:
        form = DocumentForm()
        documents = Document.objects.all().order_by('-id')
    return render(request, 'pdf_upload.html', {
        'form': form, 'documents': documents
    })

def delete_document(request,id):
    if request.method == 'POST':
        document = Document.objects.get(id=id)
        document.delete()
        return redirect('pdf_upload')