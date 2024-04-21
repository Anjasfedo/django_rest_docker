from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet

router = DefaultRouter()
router.register(r'letter', LetterViewSet)
# router.register(r'author', AuthorViewSet)
# router.register(r'user', UserViewSet)
# router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
