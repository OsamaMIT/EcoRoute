from django.db import models

class TotalProfit(models.Model):
    total = models.IntegerField(default=0)