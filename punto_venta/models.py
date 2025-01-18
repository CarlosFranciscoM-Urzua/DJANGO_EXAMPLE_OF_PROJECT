from django.db import models


# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from django.db import models

#def createBackup():
    


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_c = models.CharField(max_length=50)
    domicilio_c = models.CharField(max_length=30, blank=True, null=True)
    telefono_c = models.CharField(max_length=10, blank=True, null=True)
    e_mail_c = models.CharField(max_length=50, blank=True, null=True)
    rfc_cliente = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
    
    def __str__ (self):
        return "{}".format(self.nombre_c)


class ComprasHecha(models.Model):
    factura_compra = models.AutoField(primary_key=True)
    id_prov_c = models.ForeignKey('Proveedore', models.DO_NOTHING, db_column='id_prov_c')
    id_trab_c = models.ForeignKey('Trabajadore', models.DO_NOTHING, db_column='id_trab_c')
    fecha_c = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_hechas'
    def __str__ (self):
        return "{}".format(self.id_prov_c, ' ', self.id_trab_c)


class DetalleComprasProducto(models.Model):
    id_dcp = models.AutoField(primary_key=True)
    #factura_compra2 = models.OneToOneField(ComprasHecha, models.DO_NOTHING, db_column='factura_compra2', primary_key=True)  # The composite primary key (factura_compra2, id_prod2) found, that is not supported. The first column is selected.
    factura_compra2 = models.ForeignKey('ComprasHecha', models.DO_NOTHING, db_column='factura_compra2')
    id_prod2 = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_prod2')
    cantidad_c = models.IntegerField(blank=True, null=True)
    precio_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_compras_producto'
        unique_together = (('factura_compra2', 'id_prod2'),)

    def __str__ (self):
        return "{}".format('Producto: ', self.id_prod2, ' Factura: ', self.factura_compra2)


class DetalleVentasProducto(models.Model):
    id_dvp = models.AutoField(primary_key=True)
    id_venta2 = models.ForeignKey('VentasHecha', models.DO_NOTHING, db_column='id_venta2')
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto')
    cantidad_v = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ventas_producto'
        unique_together = (('id_venta2', 'producto'),)
    def __str__ (self):
        return "{}".format('Venta: ', self.id_venta2, ' de producto ', self.producto)
    




class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    cantidad_almacen = models.IntegerField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)
    nom_prod = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'productos'

    def __str__ (self):
        return "{}".format(self.nom_prod)


class Proveedore(models.Model):
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
    def __str__ (self):
        #return "{}".format('{self.id_prov}  EMPRESA: {self.empresa_p}')
        return "{}  EMPRESA: {}".format(self.id_prov, self.empresa_p)


class Trabajadore(models.Model):
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
    def __str__ (self):
        return "{}".format(self.nombre_t)


class VentasHecha(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    vendedor = models.ForeignKey(Trabajadore, models.DO_NOTHING, db_column='vendedor')
    factura_venta = models.IntegerField(blank=True, null=True)
    fecha_v = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_hechas'
    def __str__ (self):
        return "{}".format(self.id_venta)
