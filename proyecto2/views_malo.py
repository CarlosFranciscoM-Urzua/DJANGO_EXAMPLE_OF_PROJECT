#ESTE ES EL MALO
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import backup_database, restore_database
import os

def backup_view(request):
    """Vista para respaldar la base de datos"""
    backup_path = backup_database()
    if backup_path:
        #return HttpResponse(f"Respaldo exitoso: {os.path.basename(backup_path)}")
        #return print ("<script>window.alert(\"Respaldo exitoso\")</script>")
        return redirect ("/admin")
    else:
        #return HttpResponse("Error al realizar el respaldo")
        return print ("<script>window.alert(\"Error al realizar el respaldo\")</script>")


def restore_view(request):
    """Vista para restaurar la base de datos desde un archivo .sql"""
    if request.method == 'POST' and 'sql_file' in request.FILES:
        sql_file = request.FILES['sql_file']
        file_path = os.path.join('backups', sql_file.name)
        
        # Guardar el archivo temporalmente
        with open(file_path, 'wb') as f:
            for chunk in sql_file.chunks():
                f.write(chunk)
        
        # Restaurar la base de datos
        success = restore_database(file_path)
        if success:
            return HttpResponse("Restauración exitosa")
        else:
            return HttpResponse("Error al restaurar la base de datos")
    
    return render(request, 'restore.html')

def realizar_venta_view(request):
    return render(request, 'realizar_venta.html')
