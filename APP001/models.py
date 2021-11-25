from django.db import models


class BTCPrice(models.Model): 
    BTC_price = models.CharField(max_length=100)

    def __str__(self):
        return self.BTC_price
