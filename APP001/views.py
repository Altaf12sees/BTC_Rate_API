from django.shortcuts import render
from django.http import HttpResponse
from APP001.serialization import serializationClassModel
from APP001.models import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
APIKEY = "2CG14D4P09LYWFXH"

def index(request):
    return HttpResponse("Hello")


@api_view(['GET'])
def get_BTC_Price(request):
    get_api_url = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=2CG14D4P09LYWFXH')
    serialize = serializationClassModel(get_api_url, many=False)
    return Response(serialize.data)
