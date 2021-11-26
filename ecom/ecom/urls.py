"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ecom import settings
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("store.urls")),
    path("store/", include("store.urls"), name="store"),
    path("search", views.home, name="search"),
    # path("login/", views.home, name="login"),
    path("register", views.home, name="register"),
    path("cart", views.home, name="cart"),
    path("dashboard", views.home, name="dashboard"),
    path("logout", views.home, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
