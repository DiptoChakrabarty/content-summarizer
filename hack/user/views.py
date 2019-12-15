from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFForm,keyForm
from .models import Profile
from django.core.files.storage import FileSystemStorage
import requests
import PyPDF2
from pprint import pprint
from PyPDF2 import PdfFileReader
import io
from .cmodel import read_file
from .model import context_search

def base(request):
	if request.method=='POST' and request.FILES['myfile']:
		pdfFileObj = request.FILES['myfile'].read()
		pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdfFileObj))
		NumPages = pdfReader.numPages
		i = 0
		content=""
		while (i<NumPages):
			text = pdfReader.getPage(i)
			content+=text.extractText()
			i+=1
		return render(request,'user/base.html',{'q':1,'content':content})
		return HttpResponse(content)
	else:
		return render(request, 'user/base.html')

def keywords(request):
	if request.method == 'POST' and request.FILES['myfile']:
		pdfFileObj = request.FILES['myfile'].read()
		pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdfFileObj))
		NumPages = pdfReader.numPages
		f=keyForm(request.POST)
		a = f.get('key')
		i = 0
		content=""
		while (i<NumPages):
			text = pdfReader.getPage(i)
			content+=text.extractText()
			i+=1
		l=[]
		l=context_search(content,a)
		return HttpResponse(l)
	else:
		return render(request, 'user/base1.html')
		"""
		f=keyForm(request.POST)
		if f.is_valid():
			a = f.cleaned_data.get('key')
			l=a.split(',')
			return HttpResponse(l)
		else:
			f=keyForm()
			return render(request,'user/keywords.html',{'form':f})
	else:
		f=keyForm()
		return render(request,'user/keywords.html',{'form':f})

"""
def full(request):
	if request.method=='POST' and request.FILES['myfile']:
		pdfFileObj = request.FILES['myfile'].read()
		pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdfFileObj))
		NumPages = pdfReader.numPages
		i = 0
		content=""
		while (i<NumPages):
			text = pdfReader.getPage(i)
			content+=text.extractText()
			i+=1
		l=[]
		l=read_file(content)
		return HttpResponse(l)
	else:
		return render(request, 'user/base.html')