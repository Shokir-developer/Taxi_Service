from django.shortcuts import render, redirect
from .forms import ConatctUsForm, DamasBuyurtmaForm, NexiaBuyurtmaForm, GentraBuyurtmaForm,  HaydovchiBolibIshgaKirishForm, YukBuyurtmaForm, PochtaForm
from .models import Damaschilar, Nexiachilar, Gentrachilar, PochtaModel
def homepage(request):
	return render(request, 'index.html')


def contactUs(request):
	form = ConatctUsForm()
	if request.method == 'POST':
		form = ConatctUsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'contact.html', context)

def aboutUs(request):
	context = {}
	return render(request, 'aboutus.html', context)


def taxiService(request):
	context = {}
	return render(request, 'taxiservice.html', context)


def damaschilar(request):
	form = DamasBuyurtmaForm()
	if request.method == 'POST':
		form = DamasBuyurtmaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	queryset = Damaschilar.objects.filter(rozilik=1)
	context = {'queryset': queryset, 'form':form}
	return render(request, 'damaschilar.html', context)


def nexiachilar(request):
	form = GentraBuyurtmaForm()
	if request.method == 'POST':
		form = GentraBuyurtmaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	queryset = Nexiachilar.objects.filter(rozilik=1)
	context = {'queryset': queryset, 'form':form}
	return render(request, 'nexiachilar.html', context)

def gentrachilar(request):
	form = GentraBuyurtmaForm()
	if request.method == 'POST':
		form = GentraBuyurtmaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	queryset = Gentrachilar.objects.filter(rozilik=1)
	context = {'queryset': queryset, 'form':form}
	return render(request, 'gentrachilar.html', context)


def haydochiBolibIshga(request):
	form = HaydovchiBolibIshgaKirishForm()
	if request.method == 'POST':
		form = HaydovchiBolibIshgaKirishForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'haydovchiAriza.html', context)




def YukTashishService(request):
	context = {}
	return render(request, 'yukService.html', context)

def yuktashuvchilar(request):
	form = YukBuyurtmaForm()
	if request.method == 'POST':
		form = YukBuyurtmaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'yukTashishbuyurtma.html', context)


def pochtaService(request):
	form = PochtaForm()
	if request.method == 'POST':
		form = PochtaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form':form}
	return render(request, 'pochta.html', context)
