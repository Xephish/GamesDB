from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Developer
#from views import RestaurantCreate, DishCreate, RestaurantDetail
urlpatterns = patterns('',
        #List 5 Developers: /developers/
	url(r'^$',name='developer_list')
)
