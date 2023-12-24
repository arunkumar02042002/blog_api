from django.urls import path
# from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostViewSet, UserViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('', PostList.as_view(), name='post_list'),
#     path('users/', UserList.as_view(), name='user_list'),
#     path('users/<slug:username>/', UserDetail.as_view(), name='user_detail'),
#     path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
# ]