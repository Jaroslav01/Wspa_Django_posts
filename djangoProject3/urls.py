from django.urls import include, path
from blog import urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(urls)),
]