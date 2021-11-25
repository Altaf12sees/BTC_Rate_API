from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="API"),
    path('get_BTC_price/', views.get_BTC_Price, name="GetBTCPrice"),
    path('post_BTC_price/', views.post_BTC_Price, name="postBTCPrice")
]