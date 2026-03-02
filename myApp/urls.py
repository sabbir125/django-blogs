from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myApp import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
