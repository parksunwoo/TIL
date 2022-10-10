from Django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),
    path('<int:post_pk>/comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    #re_path(r'(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),

    path('api/post', views.post_list_create),
]









