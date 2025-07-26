# inventario/views.py
from django.views.generic import TemplateView # ¡Importante! Importamos TemplateView


class IndexView(TemplateView):
    """
    Controlador basado en clases que hereda de TemplateView.
    Este controlador se encarga de renderizar la página de inicio.
    """
    template_name = 'inventario/index.html'  # Especificamos el template a usar


class ListaProductosTemplateView(TemplateView):
    """
    Controlador basado en clases que hereda de TemplateView para
    mostrar una lista de productos de forma más concisa.
    """
    template_name = 'inventario/productos.html' # Indicamos el template directamente

    def get_context_data(self, **kwargs):
        """
        Este método se usa para añadir datos al contexto del template.
        """
        contexto = super().get_context_data(**kwargs) # Llama al método de la clase padre
        productos = [
            {'id': 1, 'nombre': 'Laptop Dell XPS 15', 'precio': 1500.00},
            {'id': 2, 'nombre': 'Teclado Mecánico RGB', 'precio': 120.00},
            {'id': 3, 'nombre': 'Monitor Curvo 27"', 'precio': 350.00},
            {'id': 4, 'nombre': 'Mouse Inalámbrico Gaming', 'precio': 75.00},
        ]
        contexto['productos'] = productos # Agregamos nuestros productos al contexto
        return contexto

# ¡Punto Clave! `TemplateView` nos permite definir el `template_name` directamente.
# La lógica para añadir datos al contexto se hace en `get_context_data()`,
# lo que mantiene nuestra lógica de negocio separada de la representación.


