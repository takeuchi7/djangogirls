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
    path('post/<int:pk>/right2/', views.post_right2, name='post_right2'),
    path('post/<int:pk>/miss2/', views.post_miss2, name='post_miss2'),
    path('post/<int:pk>/right3/', views.post_right3, name='post_right3'),
    path('post/<int:pk>/miss3/', views.post_miss3, name='post_miss3'),
    path('post/<int:pk>/right4/', views.post_right4, name='post_right4'),
    path('post/<int:pk>/miss4/', views.post_miss4, name='post_miss4'),
    path('post/<int:pk>/right5/', views.post_right5, name='post_right5'),
    path('post/<int:pk>/miss5/', views.post_miss5, name='post_miss5'),
    path('post/<int:pk>/right6/', views.post_right6, name='post_right6'),
    path('post/<int:pk>/miss6/', views.post_miss6, name='post_miss6'),
    path('post/<int:pk>/right7/', views.post_right7, name='post_right7'),
    path('post/<int:pk>/miss7/', views.post_miss7, name='post_miss7'),
    path('post/<int:pk>/right8/', views.post_right8, name='post_right8'),
    path('post/<int:pk>/miss8/', views.post_miss8, name='post_miss8'),
    path('post/<int:pk>/right9/', views.post_right9, name='post_right9'),
    path('post/<int:pk>/miss9/', views.post_miss9, name='post_miss9'),
]
