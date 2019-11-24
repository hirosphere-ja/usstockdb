from django.db import models

# Create your models here.
class Market(models.Model):
  market = models.CharField('市場', max_length=10)

  def __str__(self):
    return self.market

class Usstock(models.Model):
  ticker = models.CharField('ティッカー', max_length=5, primary_key=True)
  stockname = models.CharField('銘柄名', max_length=255)
  market = models.ForeignKey(
    Market, verbose_name='市場', on_delete=models.PROTECT,
  )

  def __str__(self):
    return '{0} {1} {2}'.format(self.ticker, self.stockname, self.exchange)
