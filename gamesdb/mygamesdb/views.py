from django.views.generic import DetailView
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


class DeveloperDetail(DetailView, ConnegResponseMixin):
    model = Developer
    template_name = 'mygamesdb/developers_detail.html'
    # def get_context_data(selfself, **kwargs):
    # context = super(DeveloperDetail, self).get_context_data(**kwargs)
    # context['RATINGS_CHOISES'] = Developer.average_videogames_rating
    # return context


class PlatformDetail(DetailView, ConnegResponseMixin):
    model = Platform
    template_name = 'mygamesdb/platforms_detail.html'


class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    template_name = 'mygamesdb/games_detail.html'
