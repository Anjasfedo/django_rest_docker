from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'letter', LetterViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]