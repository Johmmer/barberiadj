from django.contrib import admin
from .forms import CitaFormAdmin
from .models import Barbero, Servicio, Cita
from django.db.models import Q # Importar Q para OR en consultas
# Nuevo filtro personalizado
class ClienteNombreApellidoFilter(admin.SimpleListFilter):
    title = 'Filtrar por Cliente' # Título que se mostrará en el filtro
    parameter_name = 'cliente' # Nombre del parámetro en la URL
    def lookups(self, request, model_admin):
        # No necesitamos lookups predefinidos, ya que usaremos un campo de búsqueda
        # Este método es necesario pero puede devolver una lista vacía si no hay opciones fijas.
        return []
    def queryset(self, request, queryset):
        # Obtener el valor de búsqueda del parámetro 'cliente'
        cliente_query = request.GET.get(self.parameter_name)
        if cliente_query:
            # Dividir la cadena de búsqueda en palabras
            search_terms = cliente_query.split()
            # Construir una consulta OR para nombre y apellido
            query = Q()
            for term in search_terms:
                query |= Q(cliente_nombre__icontains=term) | Q(cliente_apellido__icontains=term)
            return queryset.filter(query)
        return queryset
    
@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono')
    search_fields = ('nombre', 'apellido')
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    form = CitaFormAdmin  # Usa el formulario específico para admin
    list_display = ['fecha', 'barbero', 'servicio', 'cliente_nombre', 'cliente_telefono', 'estado'] # Añadido 'estado' para mejor visibilidad
    list_filter = ['barbero', 'servicio', 'fecha', 'estado', ClienteNombreApellidoFilter] # Añadir el nuevo filtro y 'estado'
    search_fields = ['cliente_nombre', 'cliente_telefono', 'identificador'] # Mantener y añadir identificador
    date_hierarchy = 'fecha'