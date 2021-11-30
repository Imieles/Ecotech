from django.contrib import admin

from Productos.models import *

admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Comentario)


