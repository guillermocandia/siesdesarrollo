from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
        Verifica si usuario es staff o solo permite lectura.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
