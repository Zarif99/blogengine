from blog.models import Post, Tag
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView

from blog.utils import ObjectCreateMixin
from blog.utils import ObjectUpdateMixin
from blog.utils import ObjectDeleteMixin

from blog.forms import TagForm, PostForm


class PostList(ListView):
    model = Post


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'


class PostDetail(DetailView):
    model = Post


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'


class TagList(ListView):
    model = Tag


class TagCreate(ObjectCreateMixin, View):
    """
    This model create a new Tag
    """
    form = TagForm
    template = 'blog/tag_create.html'


class TagDetail(DetailView):
    """
    This model view a Tag
    """
    model = Tag


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
