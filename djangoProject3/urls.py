from django.urls import include, path
from blog import urls

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')), # Wyłączyłem wymaganą autoryzację, więc ta ścieżka nie jest już potrzebna
    path('api/', include(urls)),
]