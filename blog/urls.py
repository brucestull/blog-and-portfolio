from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_index, name='index'),
    path('<int:pk>/', views.blog_detail, name='blog-detail'),
    path('<category>/', views.blog_category, name='blog-category'),
]