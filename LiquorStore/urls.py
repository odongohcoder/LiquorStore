"""LiquorStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from LiqourApp.views import index, home, location_view
from registration import views
# from registration.views import register

app_name = 'registration'
urlpatterns = [
    # url(r'^', views.index, name='index'),
    url(r'^$', index),
    url(r'^home/', home),
    url(r'^locate/', location_view),
    url(r'^register/', views.register, name='register'),
    url(r'^admin/', include(admin.site.urls)),

]