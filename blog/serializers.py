from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_on', 'post'] # Pola z którymi będziemy pracować, które możemy zmienić, zdobyć, nadpisać

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True) # read_only=True Jest to pole tylko do pobrania, dzięki któremu możemy stworzyć artykuł bez komentarzy.
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_on', 'author', 'comment'] # Pola z którymi będziemy pracować, które możemy zmienić, zdobyć, nadpisać
