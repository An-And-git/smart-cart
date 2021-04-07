from django.db import models

CATEGORY = (('Watches', 'WATCHES'),
            ('Sun Glasses', 'SUN GLASSES'),
            ('Shoes', 'SHOES'),
            ('Bags', 'BAGS'))


class Products(models.Model):
    category = models.CharField(max_length=155, choices=CATEGORY, default='Watches')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    offer_price = models.IntegerField()

    def __str__(self):
        return self.title

    def summary(self):
        content = self.body
        spl_word = '.'
        res = content.partition(spl_word)[0]
        return res

    def offer(self):
        amount = self.price
        offer_amount = self.offer_price
        increase = amount - offer_amount
        divide = increase / amount
        result = divide * 100
        if result < 2:
            return result
        else:
            return int(result)

    def difference(self):
        amount = self.price
        offer_amount = self.offer_price
        increase = amount - offer_amount
        return increase

    def cgst(self):
        amount = self.offer_price
        cgst = (amount / 100) * 8
        return cgst

    def sgst(self):
        amount = self.offer_price
        sgst = (amount / 100) * 8
        return sgst

    def total(self):
        amount = self.offer_price
        cgst = (amount / 100) * 8
        sgst = (amount / 100) * 8
        result = cgst + sgst + amount
        return result

