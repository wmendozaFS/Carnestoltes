from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_tallas, name='pedido_home'),
]