"""API URLS"""
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()
router.register("post", PostModelViewSet, basename="post-api")

urlpatterns = router.urls
