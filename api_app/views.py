from rest_framework import viewsets, filters
from .models import Letter, Author, User, Tag
from .serializers import LetterSerializer, AuthorSerializer, UserSerializer, TagSerializer


from rest_framework.decorators import action

import django_filters.rest_framework

from .filters import LetterFilter

# from .validations import letter_query_schema

# Create your views here.


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

    filter_backends = [filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ('title', )
    filterset_class = LetterFilter

    ordering = ('id',)
    ordering_fields = ('id', 'title', 'date')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
