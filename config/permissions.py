from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user,obj.user)
        return request.user==obj.user