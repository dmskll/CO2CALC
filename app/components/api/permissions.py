from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    

class ComponentIsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.system_component:
            is_admin = request.user.is_superuser
            print(is_admin)
            print(request.user)
            return request.method in permissions.SAFE_METHODS or is_admin
    
        return obj.owner == request.user