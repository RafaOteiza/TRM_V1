from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alineacion/', views.alineacion, name='alineacion'),
    path('frenos/', views.frenos, name='frenos'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('usuario/', views.usuario, name='usuario'),
    path('motor/', views.motor, name='motor'),
    path('logout/', views.logout_view, name='logout'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
]
