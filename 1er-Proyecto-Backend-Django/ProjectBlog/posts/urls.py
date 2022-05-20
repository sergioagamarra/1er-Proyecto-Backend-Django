from django.urls import path

#from .views import posts,home,post,create_post,edit_post, delete_post

from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.posts, name='posts_list'),
    path('create', views.create_post, name='post_create'),
    path('search', views.search_post, name='post_search'),
    path('<int:id>', views.post, name='post_detail'),
    path('my-posts/<int:id>', views.my_posts, name='my_posts'),
    path('comment/<int:id>', views.create_comment, name='comment_create'),
    path('edit/<int:id>', views.edit_post, name='post_edit'),
    path('category/<int:id>', views.category_post, name='post_category'),
    path('delete-comment/<int:id>', views.delete_comment, name='comment_delete'),
    path('delete/<int:id>', views.delete_post, name='post_delete')
]
