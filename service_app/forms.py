from django import forms
from .models import ContactUs, DamasBuyurtma, NexiaBuyurtma, GentraBuyurtma,  HaydovchiBolibIshgaKirishModel, YukBuyurtmaModel, PochtaModel


class ConatctUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = '__all__'

		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter a phone  number'}),
		'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter an email'}),
		'info': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter extra info'}),

		}


class DamasBuyurtmaForm(forms.ModelForm):
	class Meta:
		model = DamasBuyurtma
		fields = '__all__'

		widgets = {
		'buyurtmachi_ismi': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'buyurtmachi_nomeri': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a nomer'}),
		'haydovchi_ismi': forms.Select(attrs={'class':'form-control', 'placeholder': 'Name of driver'}),
		'sana': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Enter a date'}),
		'vaqti': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Enter a time'}),
		

		}

class NexiaBuyurtmaForm(forms.ModelForm):
	class Meta:
		model = NexiaBuyurtma
		fields = '__all__'

		widgets = {
		'buyurtmachi_ismi': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'buyurtmachi_nomeri': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a nomer'}),
		'haydovchi_ismi': forms.Select(attrs={'class':'form-control', 'placeholder': 'Name of driver'}),
		'sana': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Enter a date'}),
		'vaqti': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Enter a time'}),
		

		}

class GentraBuyurtmaForm(forms.ModelForm):
	class Meta:
		model = GentraBuyurtma
		fields = '__all__'

		widgets = {
		'buyurtmachi_ismi': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'buyurtmachi_nomeri': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a nomer'}),
		'haydovchi_ismi': forms.Select(attrs={'class':'form-control', 'placeholder': 'Name of driver'}),
		'sana': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Enter a date'}),
		'vaqti': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Enter a time'}),
		

		}


class HaydovchiBolibIshgaKirishForm(forms.ModelForm):
	class Meta:
		model = HaydovchiBolibIshgaKirishModel
		fields = '__all__'

		widgets = {
		'ism': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'familya': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a surname'}),
		'yosh': forms.NumberInput(attrs={'class':'form-control ',  'placeholder': 'Enter your age'}),
		'soha': forms.Select(attrs={'class':'form-control mb-3',  'placeholder': 'Enter your field'}),
		

		}


class YukBuyurtmaForm(forms.ModelForm):
	class Meta:
		model = YukBuyurtmaModel
		fields = '__all__'

		widgets = {
		'ism': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'familya': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a surname'}),
		'nomer': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a phone number'}),
		'sana': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Enter a date'}),
		}

class PochtaForm(forms.ModelForm):
	class Meta:
		model = PochtaModel
		fields = '__all__'

		widgets = {
		'ism': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a name'}),
		'familya': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a surname'}),
		'nomer': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter a phone number'}),
		'viloyat': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter your region'}),
		'tuman': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter your district'}),
		'manzil': forms.TextInput(attrs={'class':'form-control ',  'placeholder': 'Enter your address'}),
		'yetib_borish_sana': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Enter a date'}),
		}
