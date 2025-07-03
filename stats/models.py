from tkinter.constants import CASCADE
from users.models import *
from django.db import models

class IncomeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)], default=1)
    import_price = models.FloatField(validators=[MinValueValidator(0.0)])

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)], default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    total_price = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    paid = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    debt = models.FloatField(validators=[MinValueValidator(0.0)], default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def calculate_total_price(self):
        if self.product.export_price:
            self.total_price = self.product.export_price * self.amount

    def save(self,*args, **kwargs):
        self.calculate_total_price()