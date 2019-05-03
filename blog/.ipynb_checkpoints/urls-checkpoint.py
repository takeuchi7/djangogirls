from django.urls import path
from . import views

urlpatterns =[
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/right/', views.post_right, name='post_right'),
    path('post/<int:pk>/miss/', views.post_miss, name='post_miss'),
    path('post/<int:pk>/right1/', views.post_right1, name='post_right1'),
    path('post/<int:pk>/miss1/', views.post_miss1, name='post_miss1'),
]
