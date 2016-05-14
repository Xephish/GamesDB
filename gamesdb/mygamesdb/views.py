from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Developer, Platform, Game
from forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator


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


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.ins_creator == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'mygamesdb/form.html'


def mainpage(request):
    return render(request, 'mygamesdb/mainpage.html')


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


class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    context_object_name = 'game'
    template_name = 'mygamesdb/games_detail.html'


class DeveloperDetail(DetailView, ConnegResponseMixin):
    model = Developer
    context_object_name = 'developer'
    template_name = 'mygamesdb/developers_detail.html'


class PlatformDetail(DetailView, ConnegResponseMixin):
    model = Platform
    context_object_name = 'platform'
    template_name = 'mygamesdb/platforms_detail.html'


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'mygamesdb/form.html'
    form_class = GameForm

    def form_valid(self, form):
        form.instance.ins_creator = self.request.user
        return super(GameCreate, self).form_valid(form)


class DeveloperCreate(LoginRequiredMixin, CreateView):
    model = Developer
    template_name = 'mygamesdb/form.html'
    form_class = DeveloperForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeveloperCreate, self).form_valid(form)


class PlatformCreate(LoginRequiredMixin, CreateView):
    model = Platform
    template_name = 'mygamesdb/form.html'
    form_class = PlatformForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlatformCreate, self).form_valid(form)


class GameDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('gamesdb:games_list')


class DeveloperDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Developer
    success_url = reverse_lazy('gamesdb:developers_list')


class PlatformDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Platform
    success_url = reverse_lazy('gamesdb:platforms_list')


# def delete_game(request,rest_pk):
#     delete_obj = Game.objects.get(pk=pk)
#     delete_obj.delete()
#     return redirect('http://127.0.0.1:8000/gamesdb/')