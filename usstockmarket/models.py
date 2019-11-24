from django.db import models

# Create your models here.
class Market(models.Model):
  market = models.CharField('市場', max_length=255)

  def __str__(self):
    return self.market
