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
    url(r'^registry', views.registry, name='registry'),
    url(r'^photo_album', views.photo_album, name='photo_album'),
    url(r'^guest_book/', views.guest_book, name='guest_book'),
    url(r'^guest_book_post/', views.guest_book_post, name='guest_book_post'),
    url(r'^program', views.program, name='program'),

)        

