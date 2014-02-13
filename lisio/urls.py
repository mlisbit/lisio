from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lisio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/$', include('resume_app.urls')),
    url(r'^projects/', include('projects_app.urls')),

    url(r'^$', include('home_app.urls')),
)
