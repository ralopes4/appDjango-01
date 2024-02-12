from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('consultar/', views.consultar_cliente, name='consultar_cliente'),
]
