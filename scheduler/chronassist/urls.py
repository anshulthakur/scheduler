'''
Created on 23-Jun-2015

@author: anshul
'''
from django.conf.urls import url, patterns

import chronassist.views as view

urlpatterns = patterns('',
        url(r'^$', view.index),
    )