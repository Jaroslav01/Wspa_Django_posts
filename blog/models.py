from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    grade = models.IntegerField()

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

class Comment(models.Model):
    author = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
