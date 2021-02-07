from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        context = {
            'form': form,
        }
        return render(request, self.template, context=context)

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        context = {
            'form': bound_form,
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context=context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        context = {
            'form': bound_form,
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj,
            'admin_object': obj
        }
        return render(request, self.template, context=context)

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
