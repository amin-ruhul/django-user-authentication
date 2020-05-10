from django.urls import path

from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('login/', views.Login,name = 'login'),
    path('registration/', views.Registration,name = 'registration'),
    path('logout/', views.Logout,name = 'logout'),
    path('edit/', views.edit_user,name = 'edit_user'),
    path('change_password/', views.change_password,name = 'change_password'),
    
]
