from rest_framework import permissions


class ObjectOwnerUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATH']:
            return obj.owner == request.user

        return True
