from django.urls import path
from .views import IndexView, ListaProductosTemplateView

app_name = 'inventario'  # Definimos el nombre de la aplicación para el namespace
urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Ruta para la página de inicio
    path('productos/', ListaProductosTemplateView.as_view(), name='productos'),

]
