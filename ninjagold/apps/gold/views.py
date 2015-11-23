from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from datetime import datetime
time = datetime.now()

def index(request):
	try:
		request.session['gold']
	except:
		request.session['gold']=0
	try:
		request.session['mymessage']
	except:
		request.session['mymessage'] = []
	return render(request, 'gold/index.html')
def process(request):
	# if 'farm_gold' in request.POST:
	if request.POST['action'] == 'farm_gold':
    		request.session['farm'] = random.randrange(10,21)
     		request.session['gold'] += request.session['farm']
    		coolness = "Earned " + str(request.session['gold']) + " from the farm! " + str(time)
    		request.session['mymessage'].insert(0,str(coolness))

  	elif request.POST['action'] == 'cave_gold':
  		request.session['cave'] = random.randrange(5,11)
  		request.session['gold'] += request.session['cave']
  		coolness = "Earned " + str(request.session['cave']) + " from the cave! " + str(time)
  		request.session['mymessage'].insert(0,str(coolness))
  		print request.session['mymessage']

  	elif request.POST['action'] == 'house_gold':
  		request.session['house'] = random.randrange(2,5)
  		request.session['gold'] += request.session['house']
  		coolness = "Earned " + str(request.session['house']) + " from the house! " + str(time)
  		request.session['mymessage'].insert(0,str(coolness))
  	
  	elif request.POST['action'] == 'casino_gold':
			request.session['casino'] = random.randrange(-50,51)
			request.session['gold'] += request.session['casino']
			if request.session['casino'] < 0:
				money = "lost " + str(request.session['casino']) + " from the casino!" + str(time)
				request.session['mymessage'].insert(0,str(money))
			else:
				money = "Earned " + str(request.session['casino']) + " from the casino!" + str(time)
				request.session['mymessage'].insert(0,str(money))
	return redirect('/')