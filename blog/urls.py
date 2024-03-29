from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed


class BlogFeed(Feed):
    title = "MySite"
    description = "Some ramblings of mine"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-fecha")[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.sumario

    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('blog.views',
                       url(r'^$',
                           ListView.as_view(queryset=Post.objects.all().order_by("-fecha")[:2],
                                            template_name="blog.html")
                           ),
                       url(r'^(?P<pk>\d+)$',
                           DetailView.as_view(model=Post,
                                              template_name="post.html")
                           ),
                       url(r'^archives/$',
                           ListView.as_view(queryset=Post.objects.all().order_by("-fecha"),
                                            template_name="archives.html")
                           ),
                       url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
                       url(r'^feed$', BlogFeed()),
                       )
