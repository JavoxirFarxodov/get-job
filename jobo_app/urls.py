from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('category/<int:type_category>', views.CategoriesView)
]