from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/champions/random', views.get_random_champion),
    re_path(r'^api/champions/(?P<id>[0-9a-zA-Z]+)$', views.champion_details),
]