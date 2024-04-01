from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=30, verbose_name='Product Name', null=False)
    brand = models.CharField(max_length=30, verbose_name='Brand', null=False)
    price = models.IntegerField(verbose_name='Price')
    quantity = models.IntegerField(verbose_name='Quantity')
    # total = models.IntegerField(verbose_name='Total')
    purchase_date = models.DateTimeField(verbose_name='Purchase Date & Time')

    def __str__(self):
        return f'{self.name} --> Rs.{self.price}'

    def __repr__(self):
        return str(self)
