from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from models import Game, Developer, Platform
# from forms import	RestaurantForm,	DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail
from views import *

urlpatterns = patterns('',

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
)