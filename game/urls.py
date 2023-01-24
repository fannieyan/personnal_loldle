from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/champions/random', views.random_champion),
    re_path(r'^api/champions/(?P<champion_id>[0-9]+)$', views.champion_details),
]