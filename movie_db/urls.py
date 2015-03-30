from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('movie_app.urls', namespace='movie_app')),
    url(r'^admin/', include(admin.site.urls)),
)
