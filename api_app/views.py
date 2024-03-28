from rest_framework import viewsets
from .models import Letter, Author
from .serializers import LetterSerializer, AuthorSerializer

# Create your views here.

class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
