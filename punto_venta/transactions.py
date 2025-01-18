from django.db import connection, IntegrityError
from django.http import JsonResponse
from django.shortcuts import render

def realizar_venta(request):
    if request.method == 'POST':
        p_id_venta = request.POST.get('id_venta')
        p_producto = request.POST.get('producto')
        p_cantidad_v = request.POST.get('cantidad_v')

        try:
            with connection.cursor() as cursor:
                cursor.callproc('verificararticuloenventa', [p_id_venta, p_producto, p_cantidad_v])
            return JsonResponse({'status': 'success', 'message': 'Venta realizada correctamente.'})
        except IntegrityError as e:
            # Capturamos los mensajes enviados desde MySQL
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error inesperado: ' + str(e)}, status=500)
    return render(request, 'realizar_venta.html')
