from django.urls import path, include
from .import views

app_name = 'album'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<id>/<str:slug>/', views.detail_view,name='details'),
    #path('search/', views.search,name='search'),
    #path('', views.login, name= 'login'),
    path('users/register/', views.register_vista, name='register'),
    path('users/login/', views.login_vista, name='login'),

]