from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'projects_app.views.home'), 
)
