from django.contrib import admin
from .models import Author, Tag, Letter, User
# Register your models here.

admin.site.register([Author, Tag, Letter, User])