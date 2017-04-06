'''
Created on Apr 6, 2017

@author: nataraja
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/$', views.get_result),

    #url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'), #by regular expression
    #url(r'^[0-9]+/$',views.test)
]