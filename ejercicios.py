import datetime

from confApp.models import *


def presentacion(n_ejercicio):
    print(f"----- EJERCICIO {n_ejercicio} -----")


presentacion(1)
clientes = Clientes.objects.all().filter(apellido__regex=r'[A-Z]{7}').order_by('-apellido')
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.apellido}")

presentacion(2)
facturas = Facturas.objects.all().filter(cod_cliente__cod_barrio__nombre='OBSERVATORIO')
for factura in facturas:
    print(f"{factura.nro_factura} {factura.cod_cliente.nombre} {factura.cod_cliente.cod_barrio.nombre}")

presentacion(3)
clientes = Clientes.objects.all().filter(cod_barrio__nombre='ALTO ALBERDI')
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.apellido} {cliente.email}")

presentacion(4)
plantas = Plantas.objects.all().filter(precio__gt=100)
for planta in plantas:
    print(f"{planta.cod_planta} {planta.descripcion} {planta.precio}")

presentacion(5)
date_start = datetime.date(2010, 1, 1)
date_end = datetime.date(2012, 12, 31)
facturas = Facturas.objects.all().filter(fecha__range=(date_start, date_end)).filter(
    cod_cliente__nombre='MARIELA').filter(cod_cliente__apellido='LEDESMA')
for factura in facturas:
    print(f"{factura.fecha} {factura.cod_cliente.nombre} {factura.cod_cliente.apellido}")
