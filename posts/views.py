from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Listing all the blogs
class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Post Detail Endpoint
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer