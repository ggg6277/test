from django.urls import path
from. import views


urlpatterns = [
    path('base/', views.base, name='base'),
    path('blog/', views.blog, name = 'blog'),
    path('blog_detail/<int:pk>', views.blog_detail, name = 'blog_detail'),
    path('base1/', views.base1, name='base1')
]