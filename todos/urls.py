from django.urls import path
from . import views

urlpatterns = [
    # Add task
    path('addTask/', views.addTask, name='addTask'),
    # Mark as Done
    path('markTask/<int:pk>/', views.markTask, name='markTask'),
    # Mark as UnDone
    path('unmarkTask/<int:pk>/', views.unmarkTask, name='unmarkTask'),
    # Edit Feature
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    # delete Feature
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
]