from django.conf.urls import patterns, include, url
from getting_married import views




urlpatterns = patterns('',
    url(r'^$',views.home,name='home'),
    url(r'^getting_married/', include('getting_married.urls')),
)
