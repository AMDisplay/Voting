from django.urls import path
from .views import Voters, views
from django.contrib.auth import views as auth_views

app_name = "foundations"


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('voters/<int:pk>/', Voters.UsersDetail, name='voters_detail'),
    path('foundation/<int:pk>/', views.FoundDetail, name='found_detail'),
    path('registration', views.Registrashion.as_view(), name='registration'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'), 

]