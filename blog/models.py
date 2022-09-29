from django.db import models

# Tutaj przechowujemy modele danych, które zostaną przekonwertowane na tabele i możemy z nich korzystać w Serializer Aby tworzyć nowe rekordy, usuwać, zmieniać i odbierać

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

class Comment(models.Model):
    author = models.TextField(default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
