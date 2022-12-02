from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "foundations"


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Seach.as_view(), name='search'),
    path('registration/', views.Registrashion.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

]