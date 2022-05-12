from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorChangeContent(BasePermission):
    def has_object_permission(self, request, view, obj):
        permission = (
            request.user == obj.author or request.method in SAFE_METHODS
        )
        return permission
