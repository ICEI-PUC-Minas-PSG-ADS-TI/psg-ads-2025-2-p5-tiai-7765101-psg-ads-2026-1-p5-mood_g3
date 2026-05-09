from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    
    path("", views.index, name="index"), 

    path("dashboard/", views.dashboard_view, name="dashboard"), 
    path("perfil/", views.profile_view, name="profile"),
    path("entry/new/", views.create_entry_view, name="create_entry"),
    path("entry/<int:pk>/edit/", views.edit_entry_view, name="edit_entry"),
    path("entry/<int:pk>/delete/", views.delete_entry_view, name="delete_entry"),
]