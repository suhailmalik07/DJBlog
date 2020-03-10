"""Blog URL Configuration"""
from django.urls import path, include
from .views import HomeView, AboutView, PostDetailView, PostCreateView, \
    PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('user/<str:username>/posts/',
         UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('api/', include("blog.api.urls"))
]
