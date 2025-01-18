import subprocess
import os
from datetime import datetime
from django.conf import settings

def backup_database():
    """Genera un archivo .sql como respaldo de la base de datos"""
    db_name = settings.DATABASES['default']['NAME']
    db_user = settings.DATABASES['default']['USER']
    db_password = settings.DATABASES['default']['PASSWORD']
    db_host = settings.DATABASES['default']['HOST']
    db_port = settings.DATABASES['default']['PORT']
    
    # Nombre del archivo de respaldo
    backup_filename = f"backup_{db_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    backup_path = os.path.join(settings.BASE_DIR, 'backups', backup_filename)
    
    try:
        # Comando para hacer el respaldo
        #command = f"mysqldump -u {db_user} -p{db_password} -h {db_host} -P {db_port} {db_name} > {backup_path}"
        command = f"mysqldump -u {db_user} -h {db_host} -P {db_port} {db_name} > {backup_path}"
        subprocess.run(command, shell=True, check=True)
        return backup_path
    except subprocess.CalledProcessError as e:
        print(f"Error al realizar el respaldo: {e}")
        return None


def restore_database(sql_file):
    """Restaura la base de datos desde un archivo .sql"""
    db_name = settings.DATABASES['default']['NAME']
    #db_name = 'punto_venta'
    db_user = settings.DATABASES['default']['USER']
    db_password = settings.DATABASES['default']['PASSWORD']
    db_host = settings.DATABASES['default']['HOST']
    db_port = settings.DATABASES['default']['PORT']
    
    try:
        # Comando para restaurar la base de datos
        #command = f"mysql -u {db_user} -p {db_password} -h {db_host} -P {db_port} {db_name} < {sql_file}"
        command = f"mysql -u {db_user} -p {db_password} {db_name} < {sql_file}"
        
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al restaurar la base de datos: {e}")
        return False
