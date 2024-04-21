from django_filters import rest_framework as filters
from .models import Letter


class LetterFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class meta:
        model = Letter
        fields = ['title']
