from django.conf.urls import patterns, include, url
from getting_married import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'getting_married.views.cover', name='cover'),
    #url(r'^getting_married', 'getting_married.views.home', name='home'),
    url(r'^$',views.cover,name='cover'),
    url(r'^getting_married/', include('getting_married.urls')),
)
