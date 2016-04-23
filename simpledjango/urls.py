from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpledjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^zip\/\d{5}', include('volatum.urls')),

    url(r'^test2/', include('volatum.urls')),

   url(r'^airport_test', 'volatum.views.airport'),

    url(r'^drone$', 'volatum.views.drone', name='drone-check'),



    url('^$', 'volatum.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

)
