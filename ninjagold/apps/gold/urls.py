from django.conf.urls import patterns, url
from apps.gold import views
urlpatterns = patterns('',
	url(r'^process/$', views.process, name="process"),
	url(r'^$', views.index, name='index'),
)