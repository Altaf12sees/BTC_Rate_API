from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('API/get_BTC_price', views.get_BTC_Price, name="GetBTCPrice")
]