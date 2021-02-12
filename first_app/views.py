from django.shortcuts import render, redirect
import random
from random import randint
from operator import add, sub
from time import strftime
from datetime import datetime

def index(request):
	if not 'counter' in request.session:
		request.session['counter'] = 0
		request.session['results'] = []
	return render(request,'index.html')
def process_money(request):
	print(request.POST['location'])
	now = datetime.now()
	date_time = now.strftime("(%Y/%m/%d) %I:%M %p")
	if request.POST['location'] == 'farm':
		random = randint(10,20)
		request.session['counter'] += random
		request.session['results'].append(f"Earned {random} golds from the farm! {date_time}")
	if request.POST['location'] == 'cave':
		random = randint(5,10)
		request.session['counter'] += random
		request.session['results'].append(f"Earned {random} golds from the cave! {date_time}")
	if request.POST['location'] == 'house':	
		random = randint(2,5)
		request.session['counter'] += random
		request.session['results'].append(f"Earned {random}  golds from the house! {date_time}")
	if request.POST['location'] == 'casino':
		random = randint(-50,50)
		request.session['counter'] += random
		if random > 0: 
			request.session['results'].append(f"Entered the casino and earned {random} golds! {date_time}")
		else:
			request.session['results'].append(f"Entered the casino and lost {random} golds...Ouch.. {date_time}")	
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')
