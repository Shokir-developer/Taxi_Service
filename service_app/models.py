from django.db import models

class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	info = models.TextField()

	def __str__(self):
		return self.name


#rtaxi service uchun

class Damaschilar(models.Model):
	STATUS = (
    (0,"YOQ"),
    (1,"HA")
			)
	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=100)
	yosh = models.IntegerField()
	tajribasi = models.IntegerField()
	rozilik = models.IntegerField(choices=STATUS, default=0)
	def __str__(self):
		return self.ism

class DamasBuyurtma(models.Model):
	buyurtmachi_ismi = models.CharField(max_length=100)
	buyurtmachi_nomeri = models.CharField(max_length=50)
	haydovchi_ismi = models.ForeignKey(Damaschilar,on_delete=models.CASCADE)
	sana = models.DateField(auto_now=False)
	vaqti = models.TimeField(auto_now=False, null=True)

	def __str__(self):
		return self.buyurtmachi_ismi


class Nexiachilar(models.Model):
	STATUS = (
    (0,"YOQ"),
    (1,"HA")
			)
	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=100)
	yosh = models.IntegerField()
	tajribasi = models.IntegerField()
	rozilik = models.IntegerField(choices=STATUS, default=0)

	def __str__(self):
		return self.ism

class NexiaBuyurtma(models.Model):
	buyurtmachi_ismi = models.CharField(max_length=100)
	buyurtmachi_nomeri = models.CharField(max_length=50)
	haydovchi_ismi = models.ForeignKey(Nexiachilar,on_delete=models.CASCADE)
	sana = models.DateField(auto_now=False)
	vaqti = models.TimeField(auto_now=False, null=True)

	def __str__(self):
		return self.buyurtmachi_ismi


class Gentrachilar(models.Model):
	STATUS = (
    (0,"YOQ"),
    (1,"HA")
			)
	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=100)
	yosh = models.IntegerField()
	tajribasi = models.IntegerField()
	rozilik = models.IntegerField(choices=STATUS, default=0)

	def __str__(self):
		return self.ism

class GentraBuyurtma(models.Model):
	buyurtmachi_ismi = models.CharField(max_length=100)
	buyurtmachi_nomeri = models.CharField(max_length=50)
	haydovchi_ismi = models.ForeignKey(Gentrachilar,on_delete=models.CASCADE)
	sana = models.DateField(auto_now=False)
	vaqti = models.TimeField(auto_now=False, null=True)

	def __str__(self):
		return self.buyurtmachi_ismi



#Haydovchi bo'lib ishga kirish formasi uchun
class HaydovchiBolibIshgaKirishModel(models.Model):
	SOHA = (
		('yengil avto', 'yengil avto'),
		('yuk avto', 'yuk avto'),
		('pochta', 'pochta'),
		)

	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=100)
	yosh = models.IntegerField()
	soha = models.CharField(max_length=50, choices=SOHA)
	#guvohnoma = models.ImageField()

	def __str__(self):
		return self.ism


class YukBuyurtmaModel(models.Model):
	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=50)
	nomer = models.CharField(max_length=50)
	sana = models.DateField(auto_now=False)

	def __str__(self):
		return self.ism


class PochtaModel(models.Model):

	ism = models.CharField(max_length=100)
	familya = models.CharField(max_length=50)
	nomer = models.CharField(max_length=50)
	viloyat = models.CharField(max_length=50)
	tuman = models.CharField(max_length=50)
	manzil = models.CharField(max_length=50)
	yetib_borish_sana = models.DateField(auto_now=False)

	def __str__(self):
		return self.ism



