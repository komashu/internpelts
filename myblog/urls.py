from django.conf.urls import url, include
from myblog.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Blog Root
    url(r'^$', list_view, name="blog_index"),

    # Posts
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),

    # Post new
    url(r'^post/new/$', post_new, name='post_new'),

    # Edit Post
    url(r'^post/(?P<post_id>\d+)/edit/$', post_edit, name='post_edit'),

    # Login
    url(r'^login/$', login, {'template_name': 'blog/login.html'}, name="login"),

    # Logout
    url(r'^logout/$', logout, {'next_page': '/blog'}, name="logout"),

    # Latest Feed
    url(r'^latest/feed/$', LatestEntriesFeed()),

    # API
    url(r'^api-auth/', include('myblog.rest_framework.urls', namespace='rest_framework')),
]