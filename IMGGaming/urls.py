from django.conf.urls import patterns, url
from IMGGaming import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_report/$', views.add_report, name='add_report'),
	url(r'^report/(?P<report_name_url>\w+)/$', views.report, name='event'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
)
