from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from apps.products.models import Manufacturer, Product

def index(request):
	return render(request,'products/index.html')