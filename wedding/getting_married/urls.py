from django.conf.urls import patterns, url

from getting_married import views



urlpatterns = patterns('',
    url(r'^$', views.cover, name='cover'),
    url(r'^home', views.home, name='home'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^wedding_event', views.wedding_event, name='wedding_event'),
    url(r'^travel', views.travel, name='travel'),
    url(r'^accommodations', views.accommodations, name='accommodations'),
    url(r'registy', views.registy, name='registy'),
)        

