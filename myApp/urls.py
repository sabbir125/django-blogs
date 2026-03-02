from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myApp import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blog')

urlpatterns = [
    # site pages
    path('', views.home, name='home'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('profile/', views.profile_page, name='profile'),

    # API endpoints
    path('api/', include(router.urls)),
]
