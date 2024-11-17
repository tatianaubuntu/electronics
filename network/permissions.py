from rest_framework import permissions


class IsActive(permissions.BasePermission):
    def has_permission(self, request, view):
        """Метод проверяет активность пользователя"""
        if request.user.is_active:
            return True
