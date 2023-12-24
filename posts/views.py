# Third Party imports
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import permissions
from rest_framework import viewsets

# Project level imports
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Django Imports
from django.contrib.auth import get_user_model

User = get_user_model()

# # Listing all the blogs
# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# # Post Detail Endpoint
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     lookup_field = 'slug'
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

'''
Utilizing the Viewsets to wrap the above views into a single viewset
'''
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     lookup_field = 'username'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer