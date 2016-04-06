from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from models import Game, Developer, Platform
# from forms import	RestaurantForm,	DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail
from views import DeveloperDetail, PlatformDetail, GameDetail

urlpatterns	= patterns('',
    # List developers list:/gamesdb
    url(r'^$',
        ListView.as_view(
            queryset=Game.objects.all(),
            context_object_name='games',
            template_name='mygamesdb/games_list.html'),
        name='games_list'),

    # Developer details, ex: /gamesdb/developers/1
    url(r'^games/(?P<pk>[a-zA-Z0-9 ]+)/$',
        GameDetail.as_view(),
        name='games_detail'),

    url(r'^$developers/$',
        ListView.as_view(
            queryset=Developer.objects.all(),
            context_object_name='developers',
            template_name='mygamesdb/developers_list.html'),
        name='developers_list'),

    url(r'^developers/(?P<pk>\d+)/$',
        DeveloperDetail.as_view(),
        name='developers_detail'),

    # Developers game details, ex/gamesdb/developers/1/games/1
    # url(r'^games/(?P<game>[a-zA-Z0-9 ]+)/developers/(?P<pk>\d+)/$',
    #    DetailView.as_view(
    #    model=Developer,
    #    template_name='mygamesdb/developers_detail.html'),
    #name='developers_detail'),

     # List platforms list :/gamesdb
    # url(r'^$',
    #   ListView.as_view(
    #       queryset = Platform.objects,
    #       context_object_name = 'platforms_list',
    #       template_name = 'mygamesdb/platforms_list.xml'),
    #   name='platforms_list'),

     # Platforms details, ex: /gamesdb/platforms/1
    url(r'^platforms/(?P<pk>[a-zA-Z0-9 ]+)/$',
        PlatformDetail.as_view(),
        name='platforms_detail'),

    # Platforms game details, ex/gamesdb/plaforms/1/games/1
    url(r'^platforms/(?P<pkr>\d+)/games/(?P<pk>\d+)/$',
        DetailView.as_view(
        model=Game,
        template_name='gamesdb/games_detail.xml'),
    name='games_detail'),
)