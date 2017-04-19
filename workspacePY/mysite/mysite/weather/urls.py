'''
Created on Apr 6, 2017

@author: nataraja
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^weather/data/$', views.real_time),
    url(r'^weather/api1_0/$', views.api1_0),
    url(r'^weather/all_plot/$', views.all_plot),
    url(r'^weather/api1_0/history/$', views.history),
    url(r'^weather/api1_0/city_list/$',views.city_list),
    url(r'^weather/api1_0/getSingleData/$', views.getSingleData),
    url(r'^weather/api1_0/getLastTempData/$',views.getLastTempData),

    

    #url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'), #by regular expression
    #url(r'^[0-9]+/$',views.test)
]