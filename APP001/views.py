from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serialization
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from decouple import config
# from crontab import CronTab
from celery import shared_task
from celery.schedules import crontab
from celery import Celery
# from celery import periodic_task
import schedule
import time
import os
import requests
import json


url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+config('API_KEY')
get_data = requests.get(url).json()

split_data = get_data.get('Realtime Currency Exchange Rate')
for key, value in split_data.items():
    if key == '5. Exchange Rate':
        exchange_rate = value

dict1 = {'BTC_price': exchange_rate}
data01 = json.dumps(dict1)

#index for test
def index(request):
    return HttpResponse("APIs<li><a href='get_BTC_price/'>GET</a></li><li><a href='post_BTC_price/'>POST</a></li>")


#API for retrive data
@api_view(['GET'])
def get_BTC_Price(request):
    get_data = requests.get(url).json()
    return JsonResponse(get_data, safe=False)


#POST API 
@api_view(['POST'])
def post_BTC_Price(request):
    serializer = serialization.SerializationClassModel(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#POST Data function
@shared_task(name="POST_data_every_hour")
def post_BTC_Exchange_Rate_Every_Hour():
    serializer = serialization.SerializationClassModel(data= views.dict1, many=False)
    if serializer.is_valid():
        serializer.save()


#shcedule task
app = Celery('PRJ001')
app.conf.beat_schedule = {
    'add-every-hour-contrab': {
        'task': 'POST_data_every_hour',
        'schedule': crontab(minute="0", hour="*"),
    },
}