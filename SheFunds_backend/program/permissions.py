from rest_framework import permissions

class IsApplicant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST': # allow POST applicant for anyone
            return True
        return False
