from django.contrib import admin
from blog.models import Tag, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body','date_pub',)
    list_filter = ('title','date_pub',)
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','slug',)
    list_filter = ('title',)
    search_fields = ('title',)
