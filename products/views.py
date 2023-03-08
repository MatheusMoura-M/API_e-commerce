from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [...]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        id_parameter = self.request.query_params.get("id")
        name_parameter = self.request.query_params.get("name")
        category_parameter = self.request.query_params.get("category")

        if id_parameter:
            return Product.objects.filter(pk=id_parameter)

        if name_parameter:
            return Product.objects.filter(name__icontains=name_parameter)

        if category_parameter:
            return Product.objects.filter(category__icontains=category_parameter)

        return super().get_queryset()

    def perform_create(self, serializer):
        return super().perform_create(serializer)
