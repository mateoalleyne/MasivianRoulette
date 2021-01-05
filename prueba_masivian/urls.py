"""prueba_masivian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from prueba_masivian.apps.roulette.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('create_player/',createPlayer,name="createPlayer"),
    path('update_player/<int:id>/',updatePlayer,name="updatePlayer"),
    path('delete_player/<int:id>/',deletePlayer,name="deletePlayer"),
    path('create_roulette/',createRoulette,name="createRoulette"),
    path('place_bet/<int:idroulette>/<int:idplayer>/',placeBet,name="placeBet"),


]
