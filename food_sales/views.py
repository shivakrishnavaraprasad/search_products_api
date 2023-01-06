from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order_Detail
from .serializers import OrderSerializer


# http://127.0.0.1:8000/api/orders/?search=Chocolate
@api_view(['GET', 'POST'])
def search_product_orders(request):
    if request.method == 'GET':
        search_product = request.GET.get('search', '')

        if search_product:
            result = Order_Detail.objects.filter(product_name__contains=search_product)

            serializer = OrderSerializer(result, many=True)
            return Response({'status': 'success', "results": serializer.data}, status=200)
        return Response({'status': 'success', "results": ''}, status=200)

    elif request.method == 'POST':
        search_product = request.POST.get("search")
        # search_product = request.query_params.get('search', None)

        if search_product:
            result = Order_Detail.objects.all().filter(product_name=search_product)[:5]
            serializer = OrderSerializer(result, many=True)

            return Response({'status': 'success', "results": serializer.data}, status=200)
        return Response({'status': 'success', "results": ''}, status=200)
