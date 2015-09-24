from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Post, Category, PostCategory

import logging

def list_all(request):
    """
    """
    list_all = Post.objects.filter(publish=True).order_by('-created_at')
    for entry in list_all:
        entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
    context = {
        'entry_list': list_all,
        'url': request.META['QUERY_STRING'],
    }
    return render(request, 'entry/all.html', context)

def list_entries(request, category=None, username=None, date=None):
    """
    List all entries, paginated
    """
    per_page = 5
    page = int(request.GET.get('page', '1'))

    if category:
        grouped_list = entries_by_category(request, category)
    elif username:
        try:
            user = User.objects.get(username=username)
            grouped_list = Post.objects.filter(author=user.id).order_by('-created_at')
        except ObjectDoesNotExist:
            grouped_list = None
    elif date:
        grouped_list = Post.objects.filter(created_at__startswith=date, publish=True).order_by('-created_at')
    else:
        grouped_list = Post.objects.filter(publish=True).order_by('-created_at')

    for entry in grouped_list:
        entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)

    total_entries = grouped_list.count()
    total_pages = (total_entries/per_page)+1

    offset = (page * per_page) - per_page
    limit = offset + per_page
    entry_list = grouped_list[offset:limit]

    context = {
        'category': category,
        'author': username,
        'date': date,
        'entry_list': entry_list,
        'url': request.META['QUERY_STRING'],
        'page_range': range(1, total_pages+1),
    }
    return render(request, 'entry/index.html', context)

def mobile(request):
    grouped_list = Post.objects.filter(publish=True).order_by('-created_at')[:5]
    for entry in grouped_list:
        entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
    entry_list = grouped_list
    context = {
        'entry_list': entry_list,
    }
    return render(request, 'entry/mobile.html', context)

def view_by_id(request, id):
    """
    """
    try:
        entry = Post.objects.get(pk=id, publish=True)
        title = entry.slug
        return HttpResponseRedirect('/view/%s/' % title)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')

def view_post(request, title):
    """
    """
    entry = None
    try:
        entry = Post.objects.get(slug=title, publish=True)
    except ObjectDoesNotExist:
        entry = None
    if entry:
        try:
            entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
            entry.body = str(entry.body)
        except ObjectDoesNotExist:
            entry.category_list = None
    context = {
        'entry': entry,
        'url': request.META['QUERY_STRING'],
    }
    return render(request, 'entry/view_post.html', context)

@login_required
def preview_post(request, title):
    """
    view an unpublished post
    TODO: make this superuser required
    """
    entry = None
    try:
        entry = Post.objects.get(slug=title)
    except ObjectDoesNotExist:
        entry = None
    logging.debug(entry)
    if entry:
        try:
            entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
            entry.body = str(entry.body)
        except ObjectDoesNotExist:
            entry.category_list = None
    context = {
        'entry': entry,
        'url': request.META['QUERY_STRING'],
    }
    return render(request, 'entry/view_post.html', context)

def entries_by_category(request, category):
    try:
        post_category = Category.objects.get(slug=category)
    except ObjectDoesNotExist:
        post_category = None
    if post_category: entry_list = Post.objects.filter(postcategory__category=post_category.id, publish=True).order_by('-created_at')
    return entry_list
