# from django.contrib.syndication.feeds import Feed
from django.contrib.syndication.views import Feed

from entry.models import Post, PostCategory

class LatestDjangoEntries(Feed):
    title = "MechanicalGirl.com | Django"
    link = "http://www.mechanicalgirl.com/"
    description = "Latest posts about Django"
    title_template = "templates/feeds/post_title.html"
    description_template = "templates/feeds/post_partial_body.html"

    def items(self):
        posts = Post.objects.filter(postcategory__category=3, publish=True).order_by('-created_at')[:5]
        return posts

    def item_description(self, item):
        return item.body


class LatestPythonEntries(Feed):
    title = "MechanicalGirl.com | Python"
    link = "http://www.mechanicalgirl.com/"
    description = "Latest posts about Python"
    title_template = "templates/feeds/post_title.html"
    description_template = "templates/feeds/post_partial_body.html"

    def items(self):
        posts = Post.objects.filter(postcategory__category=2, publish=True).order_by('-created_at')[:5]
        return posts

    def item_description(self, item):
        return item.body


class LatestEntries(Feed):
    title = "MechanicalGirl"
    link = "http://www.MechanicalGirl.com/"
    description = "Latest posts on MechanicalGirl"
    title_template = "templates/feeds/post_title.html"
    description_template = "templates/feeds/post_partial_body.html"

    def items(self):
        posts = Post.objects.filter(publish=True).order_by('-created_at')[:5]
        return posts

    def item_description(self, item):
        return item.body
