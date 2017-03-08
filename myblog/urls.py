from django.conf.urls import url
from myblog.views import detail_view, list_view
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
url(r'^login/$',
    login,
    {'template_name': 'blog/login.html'},
    name="login"),
url(r'^logout/$',
    logout,
    {'next_page': '/blog'},
    name="logout"),

]