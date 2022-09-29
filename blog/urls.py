from django.urls import include, path
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()

router.register(r'posts', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]