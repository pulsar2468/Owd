'''
Created on Apr 6, 2017

@author: nataraja
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/$', views.real_time),
    #url(r'^history/$', views.history, name='history'),
    url(r'^all_plot/$', views.all_plot),

    #url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'), #by regular expression
    #url(r'^[0-9]+/$',views.test)
]