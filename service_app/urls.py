from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage, name='home'),

    path('contact/', contactUs, name='contact_us'),
    path('about/', aboutUs, name='about_us'),

    path('taxi/', taxiService, name='taxi_service'),

    path('taxi/damas/', damaschilar, name='damas_chilar'),
    path('taxi/nexia/', nexiachilar, name='nexia_chilar'),
    path('taxi/gentra/', gentrachilar, name='gentra_chilar'),

    path('haydovchi_sahifasi/', haydochiBolibIshga, name='haydovchi_bolib'),


    path('yuk/', YukTashishService, name='yuk_tashish_service'),
    path('yuk/buyurtma/', yuktashuvchilar, name='yuk_buyurtma'),


    path('pochta/', pochtaService, name='pochta_service'),





]
