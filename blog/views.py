from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectCreateMixin
from blog.utils import ObjectDeleteMixin
from blog.utils import ObjectDetailMixin
from blog.utils import ObjectUpdateMixin


class PostList(ListView):
    model = Post
    paginator_class = Post


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'
    raise_exception = True


class TagList(ListView):
    model = Tag


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """
    This model create a new Tag
    """
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    """
    This model view a Tag
    """
    model = Tag
    template = 'blog/tag_detail.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
