from django.urls import path

from . import views

urlpatterns = [
    path('update_items', views.UpdateItems.as_view())
]
