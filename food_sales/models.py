from django.db import models

CATEGORY = (
    ('B', 'Bars'),
    ('C', 'Cookies'),
    ('CR', 'Crackers')
)

REGION = (
    ('E', 'East'),
    ('W', 'West'),
    ('N', 'North'),
    ('S', 'South')
)


class Order_Detail(models.Model):
    orderDate = models.DateField(auto_now_add=True)
    region = models.CharField(choices=REGION, max_length=1)
    city = models.CharField(max_length=50, null=True)
    category = models.CharField(choices=CATEGORY, max_length=2)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.product_name} ordered on {self.orderDate}"
