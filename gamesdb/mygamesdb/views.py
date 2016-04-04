from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import	HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from models	import Developer, Platform, Game
# from forms import	RestaurantForm,	DishForm


class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'mygamedb/developers_detail.html'
    # def get_context_data(selfself, **kwargs):
       # context = super(DeveloperDetail, self).get_context_data(**kwargs)
       # context['RATINGS_CHOISES'] = Developer.average_videogames_rating
       # return context


class PlatformDetail(DetailView):
    model = Platform
    template_name = 'mygamedb/platforms_detail.xml'


class GameDetail(DetailView):
    model = Game
    template_name = 'mygamedb/games_detail.xml'
