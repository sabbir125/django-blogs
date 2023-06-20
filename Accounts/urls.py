from django.urls import path
from Accounts import views

urlpatterns = [
    path('userProfile/',views.UserProfileView.as_view()),
    path('userProfileUpdate/<int:pk>',views.UserProfileUpdateView.as_view()),
    path('signup/',views.SingupView.as_view())
]