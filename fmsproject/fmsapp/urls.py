from django.urls import path

from . import views
urlpatterns = [
    path("login", views.loginPage, name="login"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),
    path('userlogout', views.userlogout, name='userlogout'),
    path('indexhome', views.indexhome, name='indexhome'),
    path("", views.registrationPage, name="registration"),
    path("postBook", views.postBookPage, name="postBook"),
    path("postLost", views.postLostPage, name="postLost"),
]   