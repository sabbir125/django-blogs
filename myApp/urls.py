from django.urls import path
from myApp import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('post/blog',views.post_blogView),
    path('get/blogs',views.get_all_blogView),
    path('get/blogs/<int:pk>',views.get_all_blogView),
    path('update/blogs/<int:pk>',views.update_blogView),
    path('delete/blogs/<int:pk>',views.delete_blogView),
]