# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_c = models.CharField(max_length=50)
    domicilio_c = models.CharField(max_length=30, blank=True, null=True)
    telefono_c = models.CharField(max_length=10, blank=True, null=True)
    e_mail_c = models.CharField(max_length=50, blank=True, null=True)
    rfc_cliente = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class ComprasHechas(models.Model):
    factura_compra = models.AutoField(primary_key=True)
    id_prov_c = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_prov_c')
    id_trab_c = models.ForeignKey('Trabajadores', models.DO_NOTHING, db_column='id_trab_c')
    fecha_c = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_hechas'


class DetalleComprasProducto(models.Model):
    factura_compra2 = models.OneToOneField(ComprasHechas, models.DO_NOTHING, db_column='factura_compra2', primary_key=True)  # The composite primary key (factura_compra2, id_prod2) found, that is not supported. The first column is selected.
    id_prod2 = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_prod2')
    cantidad_c = models.IntegerField(blank=True, null=True)
    precio_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_compras_producto'
        unique_together = (('factura_compra2', 'id_prod2'),)


class DetalleVentasProducto(models.Model):
    id_venta2 = models.ForeignKey('VentasHechas', models.DO_NOTHING, db_column='id_venta2')
    producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='producto')
    cantidad_v = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ventas_producto'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    cantidad_almacen = models.IntegerField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_prov = models.AutoField(primary_key=True)
    empresa_p = models.CharField(max_length=50)
    domicilio_p = models.CharField(max_length=30, blank=True, null=True)
    telefono_p = models.CharField(max_length=10, blank=True, null=True)
    e_mail_prov = models.CharField(max_length=50, blank=True, null=True)
    cred_deuda_a_favor = models.FloatField(blank=True, null=True)
    horario_atencion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Trabajadores(models.Model):
    id_t = models.AutoField(primary_key=True)
    nombre_t = models.CharField(max_length=50)
    domicilio_t = models.CharField(max_length=30, blank=True, null=True)
    telefono_t = models.CharField(max_length=10, blank=True, null=True)
    e_mail_t = models.CharField(max_length=50, blank=True, null=True)
    horario = models.CharField(max_length=60)
    imss = models.CharField(max_length=10)
    rfc = models.CharField(max_length=18, blank=True, null=True)
    sueldo_mensual = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajadores'


class VentasHechas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    vendedor = models.ForeignKey(Trabajadores, models.DO_NOTHING, db_column='vendedor')
    factura_venta = models.IntegerField(blank=True, null=True)
    fecha_v = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_hechas'
