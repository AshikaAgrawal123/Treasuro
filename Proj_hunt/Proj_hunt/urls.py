"""Proj_hunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from .views import index,register_page,rules,question,logout_page,upgrade,wind
from verify.views import gen2
from .views import leaderboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wind),
    path('register/',wind),
    path('rules',wind),
    path('question',wind),
    path('leaderboard',leaderboard),
    path('YRxJ65c32AhLRZ8rh7ID',wind),
    path('logout',wind),
    #path('upgrade',upgrade),
    path('wind',wind),
    #path('gen',gen),
    #path('abra',question),
    #path('abr',index)
]






urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
