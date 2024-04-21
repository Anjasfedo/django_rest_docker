from rest_framework import viewsets, generics, filters
from .models import Letter, Author, User, Tag
from .serializers import LetterSerializer, AuthorSerializer, UserSerializer, TagSerializer

from rest_framework.response import Response
from rest_framework.decorators import action

# from .validations import letter_query_schema

# Create your views here.


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'title', 'date')
    ordering = ('id',)
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Letter.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
