from django.urls import path
from django.conf.urls import url

from . import views
urlpatterns = [
    path('', views.index),
    url(r'^article/(?P<article_id>[0-9A-Za-z_\-]+)', views.article)
]
