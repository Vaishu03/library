# Import necessary modules from Django
from django.contrib import admin
from django.urls import path
# Import views module from the current app
from . import views

# Defining URL patterns for the Django application
urlpatterns = [
    path('', views.show), # Path for the default route ('') to the show view
    path('index',views.index), # Path for the index route to the index view
    path('show',views.show), # Path for the show route to the show view
    path('edit/<str:ISBN>',views.edit), # Path for the 'edit' route with a dynamic parameter 'ISBN' to the edit view
    path('update/<str:ISBN>',views.update), # Path for the 'update' route with a dynamic parameter 'ISBN' to the update view
    path('delete/<str:ISBN>',views.destroy) # Path for the 'delete' route with a dynamic parameter 'ISBN' to the destroy view
]