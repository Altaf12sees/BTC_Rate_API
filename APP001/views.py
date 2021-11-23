from django.shortcuts import render
from django.http import HttpResponse
from APP001.serialization import serializationClassModel
from APP001.models import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def index(request):
    return HttpResponse("Hello")


@api_view(['GET'])
def get_BTC_Price(request):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+env('API_KEY')
    get_api_url = requests.get('')
    serialize = serializationClassModel(get_api_url, many=False)
    return Response(serialize.data)

print("ppppp")