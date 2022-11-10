# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barrios(models.Model):
    cod_barrio = models.IntegerField(db_column='COD_BARRIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BARRIOS'


class Calles(models.Model):
    cod_calle = models.IntegerField(db_column='COD_CALLE', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALLES'


class Clientes(models.Model):
    cod_cliente = models.IntegerField(db_column='COD_CLIENTE', primary_key=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_calle = models.ForeignKey(Calles, models.DO_NOTHING, db_column='COD_CALLE', blank=True, null=True)  # Field name made lowercase.
    altura = models.IntegerField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    cod_barrio = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='COD_BARRIO', blank=True, null=True)  # Field name made lowercase.
    cod_localidad = models.ForeignKey('Localidades', models.DO_NOTHING, db_column='COD_LOCALIDAD', blank=True, null=True)  # Field name made lowercase.
    cod_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='COD_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    telefono = models.DecimalField(db_column='TELEFONO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cod_condicion_iva = models.ForeignKey('CondicionesIva', models.DO_NOTHING, db_column='COD_CONDICION_IVA', blank=True, null=True)  # Field name made lowercase.
    cuit = models.DecimalField(db_column='CUIT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deudor = models.CharField(db_column='DEUDOR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES'


class CondicionesIva(models.Model):
    cod_condicion_iva = models.IntegerField(db_column='COD_CONDICION_IVA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONDICIONES_IVA'


class DetallesFacturas(models.Model):
    cod_detalle = models.IntegerField(db_column='COD_DETALLE', primary_key=True)  # Field name made lowercase.
    cod_planta = models.ForeignKey('Plantas', models.DO_NOTHING, db_column='COD_PLANTA', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    nro_factura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='NRO_FACTURA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETALLES_FACTURAS'


class Facturas(models.Model):
    nro_factura = models.IntegerField(db_column='NRO_FACTURA', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    cod_forma_pago = models.ForeignKey('FormasPago', models.DO_NOTHING, db_column='COD_FORMA_PAGO', blank=True, null=True)  # Field name made lowercase.
    cod_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='COD_CLIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTURAS'


class FormasPago(models.Model):
    cod_forma_pago = models.IntegerField(db_column='COD_FORMA_PAGO', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORMAS_PAGO'


class Localidades(models.Model):
    cod_localidad = models.IntegerField(db_column='COD_LOCALIDAD', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADES'


class Plantas(models.Model):
    cod_planta = models.IntegerField(db_column='COD_PLANTA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_tipo_planta = models.ForeignKey('TiposPlantas', models.DO_NOTHING, db_column='COD_TIPO_PLANTA', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANTAS'


class Provincias(models.Model):
    cod_provincia = models.IntegerField(db_column='COD_PROVINCIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'


class TiposPlantas(models.Model):
    cod_tipo_planta = models.IntegerField(db_column='COD_TIPO_PLANTA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_PLANTAS'


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
