from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('django.views.generic.simple',
    (r'^resume/$',    TemplateView.as_view(template_name="pages/resume.html")),
    (r'^about/$',     TemplateView.as_view(template_name="pages/about.html")),
    (r'^$',           TemplateView.as_view(template_name="pages/about.html")),
)
