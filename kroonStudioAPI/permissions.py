from rest_framework import permissions


class ArticleEditPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.created_by_user_id == request.user


class CategoryEditPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
