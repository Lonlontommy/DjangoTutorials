from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'create_blog$', views.create_blog, name='create_blog'),
]
