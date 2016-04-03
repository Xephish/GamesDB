from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Game, Developer, Platform
# from forms import	RestaurantForm,	DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail
from views import DeveloperDetail, PlatformDetail

urlpatterns	= patterns('',
    # List developers list:/gamesdb
    url(r'^$',
        ListView.as_view(
            queryset = Developer.objects,
            context_object_name = 'developers_list',
            template_name = 'mygamesdb/developers_list.xml'),
        name = 'developers_list'),

    # Developer details, ex: /gamesdb/developers/1
    url(r'^developers/(?P<pk>\d+)/$',
        DeveloperDetail.as_view(),
        name = 'developers_detail'),

    # Developers game details, ex/gamesdb/developers/1/games/1
    url(r'^developers/(?P<pkr>\d+)/games/(?P<pk>\d+))/$',
        DetailView.as_view(
        model = Game,
        template_name= 'gamesdb/games_detail.xml'),
    name='games_detail'),

     # List platforms list :/gamesdb
    url(r'^$',
        ListView.as_view(
            queryset = Platform.objects,
            context_object_name = 'platforms_list',
            template_name = 'mygamesdb/platforms_list.xml'),
        name = 'platforms_list'),

     # Platforms details, ex: /gamesdb/platforms/1
    url(r'^platforms/(?P<pk>\d+)/$',
        PlatformDetail.as_view(),
        name = 'platforms_detail'),

    # Platforms game details, ex/gamesdb/plaforms/1/games/1
    url(r'^platforms/(?P<pkr>\d+)/games/(?P<pk>\d+))/$',
        DetailView.as_view(
        model = Game,
        template_name= 'gamesdb/games_detail.xml'),
    name='games_detail'),
)