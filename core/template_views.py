# template_views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout

def google_login_view(request):
    return render(request, "google_login.html")

def logout_view(request):
    logout(request)
    return redirect("/")
