# urls.py
from django.urls import path
from .views import create_portfolio, update_portfolio, delete_portfolio, portfolio_list

urlpatterns = [
    path('portfolio/create/', create_portfolio, name='portfolio-create'),
    path('portfolio/<int:pk>/update/', update_portfolio, name='portfolio-update'),
    path('portfolio/<int:pk>/delete/', delete_portfolio, name='portfolio-delete'),
    path('portfolios/', portfolio_list, name='portfolio-list'),
]
