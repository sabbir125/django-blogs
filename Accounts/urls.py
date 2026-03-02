from django.urls import path
from accounts import views

urlpatterns = [
    path('userProfile/', views.UserProfileView.as_view(), name='user-profile'),
    path('userProfileUpdate/<int:pk>', views.UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('signup/', views.SignupView.as_view(), name='signup')
]