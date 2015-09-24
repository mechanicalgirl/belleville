from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from belleville.feeds import LatestPythonEntries, LatestDjangoEntries, LatestEntries

feeds = {
    'python': LatestPythonEntries,
    'django': LatestDjangoEntries,
    'all': LatestEntries,
}

urlpatterns = patterns('',
    url(r'^post/', include('entry.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('entry.urls')),
    url(r'^feeds/(?P<url>.*)/$', LatestEntries()),
)
