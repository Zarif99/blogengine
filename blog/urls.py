from django.urls import path
from blog.views import post_list, PostDetail, tags_list, TagDetail
from blog.views import TagCreate

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('blog/tags/', tags_list, name='tags_list_url'),
    path('blog/tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('blog/tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('blog/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
]
