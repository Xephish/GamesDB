from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers

from models import Developer, Platform, Game


# from forms import	RestaurantForm,	DishForm

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)


class GamesList(ListView, ConnegResponseMixin):
    model = Game
    queryset = Game.objects.all()
    context_object_name = 'games'
    template_name = 'mygamesdb/games_list.html'


class DevelopersList(ListView, ConnegResponseMixin):
    model = Developer
    queryset = Developer.objects.all()
    context_object_name = 'developers'
    template_name = 'mygamesdb/developers_list.html'


class PlatformsList(ListView, ConnegResponseMixin):
    model = Platform
    queryset = Platform.objects.all()
    context_object_name = 'platforms'
    template_name = 'mygamesdb/platforms_list.html'


class DeveloperDetail(DetailView, ConnegResponseMixin):
    model = Developer
    context_object_name = 'platforms'
    template_name = 'mygamesdb/developers_detail.html'


class PlatformDetail(DetailView, ConnegResponseMixin):
    model = Platform
    template_name = 'mygamesdb/platforms_detail.html'


class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    template_name = 'mygamesdb/games_detail.html'
