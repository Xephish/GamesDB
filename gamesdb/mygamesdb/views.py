from django.views.generic import DetailView

from models import Developer, Platform, Game


# from forms import	RestaurantForm,	DishForm


class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'mygamesdb/developers_detail.html'
    # def get_context_data(selfself, **kwargs):
    # context = super(DeveloperDetail, self).get_context_data(**kwargs)
    # context['RATINGS_CHOISES'] = Developer.average_videogames_rating
    # return context


class PlatformDetail(DetailView):
    model = Platform
    template_name = 'mygamesdb/platforms_detail.xml'


class GameDetail(DetailView):
    model = Game
    template_name = 'mygamesdb/games_detail.xml'
