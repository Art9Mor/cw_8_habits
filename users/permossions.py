from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    massage = "You are not allowed to access this actions"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return request.method in ('GET', 'PUT', 'PATCH', 'DELETE')
        return False
