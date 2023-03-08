from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from utils.permissions import AdminOrOwnerPermissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAdminUser()]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrOwnerPermissions]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None
    lookup_url_kwarg = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
