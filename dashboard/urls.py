from django.urls import path
from .views import Home, Favorite, ViewMap


urlpatterns = [
    path('', Home, name='home-page'),
    path('favorite', Favorite, name='favorite-page'),
    path('viewmap', ViewMap, name='viewmap-page'),

    

    
]
