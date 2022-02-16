from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveIntegerField(verbose_name=_('discount'))
    short_description = models.TextField(verbose_name=_('short description'))
    long_description = models.TextField(verbose_name=_('long description'))

    def get_price(self):
        if self.discount == 0:
            return self.price
        return self.price - (self.price / 100) * self.discount
