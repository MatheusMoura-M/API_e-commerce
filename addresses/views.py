from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [...]

    queryset = ...
    serializer_class = ...
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        return super().perform_create(serializer)
