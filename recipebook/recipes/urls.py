from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('logout/', views.logout_view, name='logout'),
]