from django.shortcuts import render, redirect
from django.urls import reverse

from blog.models import Post, Tag
from django.views.generic import View

from blog.utils import ObjectCreateMixin
from blog.utils import ObjectDetailMixin
from blog.utils import ObjectUpdateMixin
from blog.utils import ObjectDeleteMixin

from blog.forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'
    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/post_delete.html', context={'post': post})
    #
    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     post.delete()
    #     return redirect(reverse('post_list_url'))


class TagCreate(ObjectCreateMixin, View):
    """
    This model create a new Tag
    """
    form = TagForm
    template = 'blog/tag_create.html'


class TagDetail(ObjectDetailMixin, View):
    """
    This model view a Tag
    """
    model = Tag
    template = 'blog/tag_detail.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete.html',context={'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))