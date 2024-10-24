# template_urls.py

from django.urls import path
from .template_views import google_login_view, logout_view

urlpatterns = [
    path("google_login_view/", google_login_view, name="google_login_view"),
    path("logout/", logout_view, name="logout"),
]
