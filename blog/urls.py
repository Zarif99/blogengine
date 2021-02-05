from django.urls import path
from blog.views import post_list, post_detail, tags_list, tag_detail

urlpatterns = [
    path('', post_list , name='post_list_url'),
    path('blog/tags/', tags_list, name='tags_list_url'),
    path('blog/tag/<str:slug>', tag_detail, name='tag_detail_url'),
    path('blog/<str:slug>/', post_detail, name='post_detail_url'),

]