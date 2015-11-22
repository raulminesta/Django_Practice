from django.shortcuts import render
def index(request):
	return render(request,'ninja/index.html')
def show(request, color):
	context = {'color': color }
	return render(request, 'ninja/show.html', context)