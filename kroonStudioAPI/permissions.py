from rest_framework import permissions


class ArticleEditPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'PATCH':
            return False
        return obj.created_by_user_id == request.user or request.user.is_superuser
