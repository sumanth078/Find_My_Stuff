"""
URL configuration for fmsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.registrationPage,name="registration"),
    path("index",views.indexpage,name="index"),
    path("aboutus",views.aboutuspage,name="aboutus"),
    path("contactus",views.contactuspage,name="contactus"),
    path("test",views.testpage,name="test"),
    path("",include("fmsapp.urls")),
]
