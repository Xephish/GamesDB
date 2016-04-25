from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView
from models import Game, Developer, Platform
from views import *

urlpatterns = [

    url(r'^$',
        GamesList.as_view(),
        name='games_list'),

    url(r'^api\.(?P<extension>(json|xml|html))/$',
        GamesList.as_view(),
        name='games_list_api'),

    url(r'^developers/$',
        DevelopersList.as_view(),
        name='developers_list'),

    url(r'^developersapi\.(?P<extension>(json|xml|html))/$',
        DevelopersList.as_view(),
        name='developers_list_api'),

    url(r'^platforms/$',
        PlatformsList.as_view(),
        name='platforms_list'),

    url(r'^platformsapi\.(?P<extension>(json|xml|html))/$',
        PlatformsList.as_view(),
        name='platforms_list_api'),

    url(r'^games/(?P<pk>[a-zA-Z0-9 ]+)/$',
        GameDetail.as_view(),
        name='games_detail'),

    url(r'^developers/(?P<pk>[a-zA-Z0-9 ]+)/$',
        DeveloperDetail.as_view(),
        name='developers_detail'),

    url(r'^platforms/(?P<pk>[a-zA-Z0-9 ]+)/$',
        PlatformDetail.as_view(),
        name='platforms_detail'),

    url(r'^games/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Game,
            template_name='mygamesdb/form.html',
            form_class=GameForm),
        name='game_edit'),

    url(r'^developers/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Developer,
            template_name='mygamesdb/form.html',
            form_class=DeveloperForm),
        name='developer_edit'),

    url(r'^platforms/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Platform,
            template_name='mygamesdb/form.html',
            form_class=PlatformForm),
        name='platform_edit'),

    url(r'^gamesapi/(?P<pk>[a-zA-Z0-9 ]+)\.(?P<extension>(json|xml|html))/$',
        GameDetail.as_view(),
        name='games_detail_api'),

    url(r'^developersapi/(?P<pk>[a-zA-Z0-9 ]+)\.(?P<extension>(json|xml|html))/$',
        DeveloperDetail.as_view(),
        name='developers_detail_api'),

    url(r'^platformsapi/(?P<pk>[a-zA-Z0-9 ]+)\.(?P<extension>(json|xml|html))/$',
        PlatformDetail.as_view(),
        name='platforms_detail_api'),

    url(r'^gamesdb/create/$',
        GameCreate.as_view(),
        name='game_create'),

    url(r'^gamesdb/developers/create/$',
        DeveloperCreate.as_view(),
        name='developer_create'),

    url(r'^gamesdb/platforms/create/$',
        PlatformCreate.as_view(),
        name='platform_create'),
]