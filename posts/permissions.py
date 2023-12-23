from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        # Read-only permissions are allowed for all authenticated users
        if request.method in SAFE_METHODS: # (GET, HEAD, OPTIONS)
            return True
        
        # Write permissions are only allowed to the author of the blog
        return obj.author == request.user