from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('irish_townlands.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
