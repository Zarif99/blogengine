from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from blog.models import Post, Tag
from blog.forms import PostForm, TagForm


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    template = None

    def get(self, request, slug):
        post = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = PostForm(instance=post)
        context={
            'form': bound_form,
            'post': post
        }
        return render(request, self.template, context=context)

    def post(self, request, slug):
        post = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        context = {
            'form': bound_form,
            'post': post
        }
        return render(request, self.template, context=context)
