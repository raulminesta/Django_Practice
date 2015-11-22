from django.conf.urls import patterns, url
from apps.survey import views
urlpatterns = patterns('',
	url(r'^process_form/$', views.process_form, name="process_form"),
	url(r'^result/$',views.result, name="result"),
	url(r'^$', views.index, name='index'),
)