from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)
admin.site.site_header = "RecipeBook Admin"
admin.site.site_title = "Recipebook Portal"
admin.site.index_title = "Welcome to the RecipeBook Management System"