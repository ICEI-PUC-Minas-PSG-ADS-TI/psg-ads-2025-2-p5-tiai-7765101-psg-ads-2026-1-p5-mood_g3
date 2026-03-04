from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("entry/new/", views.create_entry_view, name="create_entry"),
]
