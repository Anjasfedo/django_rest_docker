from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, AuthorViewSet, UserViewSet

router = DefaultRouter()
router.register(r'letter', LetterViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'user', UserViewSet)
# router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
