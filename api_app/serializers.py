from rest_framework import serializers
from .models import Letter, Author, User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'


class LetterSerializer(serializers.ModelSerializer):
    sender = AuthorSerializer()
    receiver = UserSerializer()
    # tag = TagSerializer(many=True)

    class Meta:
        model = Letter
        fields = ['title', 'body', 'date', 'number', 'is_done', 'sender', 'receiver']
