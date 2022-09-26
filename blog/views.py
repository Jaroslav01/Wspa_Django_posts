from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from blog.serializers import UserSerializer
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_on')
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

