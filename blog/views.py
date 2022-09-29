from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on') # Sortuj artykuły według daty utworzenia
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_on') # Komentarze sortujemy według daty utworzenia, chociaż nie musimy otrzymywać listy osobno przez /api/coments/,  użyjemy więcej tworzyć, usuwać, edytować
    serializer_class = CommentSerializer

