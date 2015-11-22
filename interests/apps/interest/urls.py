from django.conf.urls import patterns, url     # import functions to match patterns
from apps.interest import views                    # import views.py file from our quiz app
urlpatterns = patterns('',
	url(r'^users/(?P<user_id>\d+)/$',views.show_user, name="show_user"),
	url(r'^$', views.index, name='index'),
	url(r'^interests/$', views.show, name='interests'),
)