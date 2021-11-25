from . import serialization
from . import views

print("tasking....")
#create exchange rate data in every hour
def updatebtc():
    serializer = serialization.SerializationClassModel(data= views.dict1, many=False)
    if serializer.is_valid():
        serializer.save()
updatebtc()