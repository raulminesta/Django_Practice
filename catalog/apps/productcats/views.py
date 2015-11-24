from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from apps.productcats.models import Manufacturer, Product
from django.utils import timezone
def index(request):
	products = Product.objects.all().select_related('manufacturer')
	context = {
		'products': products
	}
	return render(request,'productcats/index.html', context)
def show(request, product_id): #will need an id passed through
	products= Product.objects.filter(id=product_id).select_related('manufacturer')[0]
	context={
		'products': products
	}
	return render(request,'productcats/show.html', context)
def create(request):
	insert = Product(name= request.POST['name'], price = request.POST['price'], created_at= timezone.now(), manufacturer= Manufacturer.objects.get(name=request.POST['manname']), description= request.POST['description'])
	print insert.name
	insert.save()
	return redirect('/')
def delete(request, product_id):
	Product.objects.get(id=product_id).delete()
	return redirect('/')
def update(request, product_id):
	product= Product.objects.get(id=product_id).update(name=request.POST['name'], price= request.POST['price'],created_at=timezone.now(),manufacturer= Manufacturer.objects.get(name=request.POST['manname']), description = request.POST['description'])
	context={
		'product': product
	}
	return render(request,'productcats/index.html', context)