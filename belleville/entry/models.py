from django.db import models
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Post(models.Model):
    """
    """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/post/%s/" % self.slug

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    """
    """
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

class PostCategory(models.Model):
    """
    """
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = "post categories"
