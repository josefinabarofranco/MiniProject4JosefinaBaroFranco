from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),

    path('recipe_list/', views.recipe_list, name='recipe_list'),

    path('user_dash/', views.user_dash, name='user_dash'),

    path('logout/', views.logout_view, name='logout'),

]