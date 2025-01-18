from django.contrib import admin
import os
from datetime import datetime

from .models import *

admin.site.register(Cliente)
admin.site.register(ComprasHecha)
admin.site.register(DetalleComprasProducto)
admin.site.register(DetalleVentasProducto)
admin.site.register(Producto)
admin.site.register(Proveedore)
admin.site.register(Trabajadore)
admin.site.register(VentasHecha)

admin.site.site_header="INFINITO - PUNTO DE VENTA"
admin.site.site_title="INFINITO - PUNTO DE VENTA"
admin.site.index_title="CIBER INFINITO - ADMINISTRACION PUNTO DE VENTA"

"""def createBackup():
    os.system(f"python manage.py dumpdata --indent 2 > respaldo{datetime.datetime.now()}.json")"""
# Register your models here.
