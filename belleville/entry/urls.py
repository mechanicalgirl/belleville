from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^post/(?P<title>.*?)/*$',           views.view_post,         name='entry_view'),
    url(r'^view/(?P<title>.*?)/*$',           views.view_post,         name='entry_view'),

    url(r'^viewid/(?P<id>\w+)/*$',            views.view_by_id,        name='entry_viewbyid'),
    url(r'^preview/(?P<title>.*?)/*$',        views.preview_post,      name='entry_preview'),

    url(r'^all/*$',                           views.list_all,          name='entry_list_all'),

    url(r'^mobile/*$',                        views.mobile,            name='entry_mobile'),
    url(r'^category/(?P<category>.*?)/*$',    views.list_entries,      name='entry_list'),
    url(r'^author/(?P<username>.*?)/*$',      views.list_entries,      name='entry_list'),
    url(r'^date/(?P<date>.*?)/*$',            views.list_entries,      name='entry_list'),

    url(r'^$',                                views.list_entries,      name='entry_list'),
)
