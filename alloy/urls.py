"""
URL configuration for alloy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from predictions import views
from django.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.png', permanent=True)),
    path('', views.homepage, name='homepage'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    #path("__debug__/", include("debug_toolbar.urls")),
    path("analysis/", include("predictions.urls")),
    path('admin/', admin.site.urls),
]
