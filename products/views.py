from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
import ipdb


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [...]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ProductDetailView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [...]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        # ipdb.set_trace()
        return Product.objects.filter(pk=self.kwargs["product_id"])

    def perform_create(self, serializer):
        return super().perform_create(serializer)
