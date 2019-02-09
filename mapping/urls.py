"""mapping URL Configuration

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
from django.urls import path, include

from mapping import views
from mapping.views import *

app_name='mapping'
urlpatterns = [
    path('', MedimageLV.as_view(), name='index'),
    path('medimage/', MedimageLV.as_view(), name='medimage_list'),
    path('before/', BeforeLV.as_view(), name='medimage_before'),
    path('after/', AfterLV.as_view(), name='medimage_after'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('medimage/<int:pk>', MedimageDV.as_view(), name='medimage_detail'),
]