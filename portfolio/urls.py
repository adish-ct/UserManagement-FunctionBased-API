from django.urls import path
from .views import portfolio_view, login_view, update_profile, delete_user

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
]