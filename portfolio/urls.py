# urls.py
from django.urls import path
from .views import create_portfolio, update_portfolio, delete_portfolio, \
    portfolio_list, create_project, update_project, delete_project, create_skill, update_skill, delete_skill

urlpatterns = [
    path('portfolio/create/', create_portfolio, name='portfolio-create'),
    path('portfolio/<int:pk>/update/', update_portfolio, name='portfolio-update'),
    path('portfolio/<int:pk>/delete/', delete_portfolio, name='portfolio-delete'),
    path('portfolios/', portfolio_list, name='portfolio-list'),
    path('portfolio/<int:portfolio_id>/project/create/', create_project, name='project-create'),
    path('portfolio/project/<int:pk>/update/', update_project, name='project-update'),
    path('portfolio/project/<int:pk>/delete/', delete_project, name='project-delete'),
    path('portfolio/<int:portfolio_id>/skill/create/', create_skill, name='skill-create'),
    path('portfolio/skill/<int:pk>/update/', update_skill, name='skill-update'),
    path('portfolio/skill/<int:pk>/delete/', delete_skill, name='skill-delete'),

]
