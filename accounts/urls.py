from django.urls import path
from .views import register, login_view, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/update/', update_profile, name='profile-update'),
]