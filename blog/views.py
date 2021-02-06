from django.shortcuts import render, redirect

from blog.models import Post, Tag
from django.views.generic import View

from blog.utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin

from blog.forms import TagForm, PostForm
from django.shortcuts import get_object_or_404


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
    template = 'blog/post_update.html'


class TagDetail(ObjectDetailMixin, View):
    """
    This model view a Tag
    """
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    """
    This model create a new Tag
    """
    form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        context = {'form': bound_form, 'tag': tag}
        return render(request, 'blog/tag_update.html', context=context)

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        context = {
            'form': bound_form,
            'tag': tag
        }
        return render(request, 'blog/tag_update.html', context=context)
