from rest_framework import serializers
from .models import Letter, Author, User, Tag

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LetterSerializer(serializers.ModelSerializer):
    sender = AuthorSerializer()  # Assuming 'author' is a ForeignKey relation in Letter model
    # Assuming 'user' is a ForeignKey relation in Letter model
    receiver = UserSerializer()
    # Assuming 'tags' is a ManyToManyField relation in Letter model
    tag = TagSerializer(many=True)

    class Meta:
        model = Letter
        fields = '__all__'

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
