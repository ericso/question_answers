from django.conf.urls import patterns, url

from questions import views

urlpatterns = patterns('',
  url(r'^$', views.questions, name='questions'),
  url(r'^(?P<q_id>[0-9]+)/(?P<a_id>[0-9]+)/$', views.questions, name='answer'),
)
