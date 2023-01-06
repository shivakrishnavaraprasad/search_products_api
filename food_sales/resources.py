from import_export import resources
from .models import Order_Detail

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order_Detail