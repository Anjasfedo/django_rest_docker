from rest_framework import viewsets, filters
from .models import Letter, Author, User, Tag
import django_filters.rest_framework
from .serializers import LetterSerializer, AuthorSerializer, UserSerializer, TagSerializer
from .filters import LetterFilter, AuthorFilter, TagFilter, UserFilter

# Create your views here.


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    filterset_class = LetterFilter

    filter_backends = [filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend]

    ordering = ('id',)
    ordering_fields = ('id', 'title', 'date')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter

    filter_backends = [filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend]

    ordering = ('id',)
    ordering_fields = ('id', 'name')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    filter_backends = [filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend]

    ordering = ('id',)
    ordering_fields = ('id', 'name')


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter

    filter_backends = [filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend]

    ordering = ('id',)
    ordering_fields = ('id', 'name')
