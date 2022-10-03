from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Class to check if user should be permitted access
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user