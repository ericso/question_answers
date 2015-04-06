from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Gets the SPA to the user, not used for now
    # url(r'^$', 'clariture.views.home', name='home'),
    url(r'^question/', include('questions.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
