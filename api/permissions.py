from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # allow owners to edit objects
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user