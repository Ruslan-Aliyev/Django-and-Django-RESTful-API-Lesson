from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
	return render(request, 'home.html', {'name':'someone'});	

def add(request):
	no1 = int(request.POST['no1'])
	no2 = int(request.POST['no2'])
	result = no1 + no2

	return render(request, 'result.html', {'result':result});	
	