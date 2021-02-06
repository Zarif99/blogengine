from django.urls import path
from blog.views import post_list, PostDetail, tags_list, TagDetail
from blog.views import TagCreate, PostCreate, TagUpdate, PostUpdate

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/tags/', tags_list, name='tags_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('post/tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('post/tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
]
