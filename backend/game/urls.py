from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/champion/random', views.get_random_champion),
    path('api/champion/check', views.check_champion),
    path('api/champion', views.search_champion),
    re_path(r'^api/champion/(?P<id>[a-zA-Z\' \.]+)$', views.champion_details),
]
