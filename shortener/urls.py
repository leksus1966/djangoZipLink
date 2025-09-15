from django.urls import path
from .views import ShortURLCreateView, redirect_view

urlpatterns = [
    path("create/", ShortURLCreateView.as_view(), name="create"),
    path("<str:code>/", redirect_view, name="redirect"),
]
