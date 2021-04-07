from django.db import models

CATEGORY = (('Watches', 'WATCHES'),
            ('Sun Glasses', 'SUN GLASSES'),
            ('Shoes', 'SHOES'),
            ('Bags', 'BAGS'))


class Product_home(models.Model):
    category = models.CharField(max_length=155, choices=CATEGORY, default='Watches')
    title = models.CharField(max_length=255, default='title')
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default='1000')
    offer_price = models.IntegerField(default='500')

    def __str__(self):
        return self.title
