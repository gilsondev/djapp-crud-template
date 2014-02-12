from django.conf.urls import patterns, url

from .views import {{ app_name|title }}List, {{ app_name|title }}New, {{ app_name|title }}Update, {{ app_name|title }}Delete

urlpatterns = patterns('',
    url(r'^{{ app_name }}/$', {{ app_name|title }}List.as_view(), name='list'),
    url(r'^{{ app_name }}/new/$', {{ app_name|title }}New.as_view(), name='new'),
    url(r'^{{ app_name }}/(?P<slug>[\w-]+)/update/$',
        {{ app_name|title }}Update.as_view(), name='update'),
    url(r'^{{ app_name }}/(?P<slug>[\w-]+)/delete/$',
        {{ app_name|title }}Delete.as_view(), name='delete'),
)
