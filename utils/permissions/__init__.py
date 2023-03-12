from users.models import User
from rest_framework import permissions
from rest_framework.views import Request, View


class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_superuser


class AdminOrClientPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and not request.user.is_seller or request.user.is_superuser


class AdminOrSellerPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_seller or request.user.is_superuser


class ClientPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and not request.user.is_seller


class SellerPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_seller


class AdminOrOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User):
        return request.user.is_authenticated and request.user.is_superuser or user.email == request.user.email


class AdminOrProductOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User):
        return request.user.is_authenticated and request.user.is_superuser or user.email == request.user.email
