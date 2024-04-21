from django_filters import rest_framework as filters
from .models import Letter, Author, Tag, User


class LetterFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class meta:
        model = Letter
        fields = ['title']


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class meta:
        model = Author
        fields = ['name']


class TagFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class meta:
        model = Tag
        fields = ['name']


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class meta:
        model = User
        fields = ['name']
