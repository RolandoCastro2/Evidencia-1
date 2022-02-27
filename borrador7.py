from collections import namedtuple

ciclo = True
datos_productos = {}
Venta = namedtuple("Venta", ("folio_unico","fecha","descripcion","cantidad","precio_unitario"))
monto_total = 0
datos_venta = {}
clave = 1

cliente = input("Cliente al que se le realizó la venta: ")
while ciclo:
    print("\n---Registrar Venta---")
    print("[1]- Registrar")
    print("[2]- Consulta de datos")
    print("[3]- Consultar datos mediante fecha")
    print("[4]- Salir")
    print("-"*30)
    opcion = int(input(("Indique que opcion desea: ")))

    if opcion == 1:
        bolsa = []
        ciclo2 = True
        folio = int(input("Indique numero de folio unico: "))
        fecha = input("Fecha de la venta en formato (dd/mm/aaaa): ")

        while ciclo2:
            descripcion = input("Indique la descripcion del equipo: ")
            cantidad = int(input("Indique la cantidad de artículos: "))
            precio_unitario = float(input("Indique el precio unitario para este artículo: "))
            detalle = Venta( folio,fecha, descripcion, cantidad, precio_unitario)
            bolsa.append(detalle)
            opcion_Agregar = input("Deseas agregar otro articulo? S/N: ").upper()
            if opcion_Agregar == "N":
                ciclo2 = False
        else:
            monto = (cantidad * precio_unitario)
            monto_total = monto
            IVA = (monto_total * 0.16)
            monto_con_iva = monto_total + IVA
            datos_venta[folio] = [bolsa,fecha,IVA,monto_con_iva]
            print(f"\nEl total de la venta antes de impuestos es de ${monto:.2f}")
            print(f"\nEl cargo generado es de: {IVA}")
            print(f"\nEl monto total a pagar es : {monto_con_iva:.2f}")
            print("\nEl listado de la venta es: ")
            print(f"\nVenta realizada a {cliente} con fecha de {fecha}")
            print("-" * 55)
            print("Clave del artículo\tDescripcion\tCantidad\tPrecio Unitario")
            for detalle in bolsa:
                print(f"{detalle.folio_unico}\t\t\t{detalle.descripcion}\t\t\t{detalle.cantidad}\t\t${detalle.precio_unitario:.2f}")
            print("-" * 55)

    if opcion == 2:
        consulta = int(input("Ingrese el folio"))
        if consulta in datos_venta.keys():
            print(f"El folio es: {consulta}")
            print(f"Su fecha de venta es: {fecha}")
            print("-" * 50)

            print(f"\nEl total de la venta antes de impuestos es de ${monto:.2f}")
            print(f"\nEl cargo generado es de: {IVA}")
            print(f"\nEl monto total a pagar es : {monto_con_iva:.2f}")
            print("\nEl listado de la venta es: ")
            print(f"\nVenta realizada a {cliente} con fecha de {fecha}")
            print("-" * 55)
            print("Clave del artículo\tDescripcion\tCantidad\tPrecio Unitario")
            for detalle in bolsa:
                print(f"{detalle.folio_unico}\t\t\t{detalle.descripcion}\t\t\t{detalle.cantidad}\t\t${detalle.precio_unitario:.2f}")
                print("-" * 55)

    if opcion == 3:
        consulta_fecha = input("Fecha de la venta en formato (dd/mm/aaaa): ")
        for claves in datos_venta.keys():
            for dato in datos_venta[claves][0]:
                if consulta_fecha in dato.fecha:
                    print(f"Su fecha de venta es: {dato.fecha}")
                    print("-" * 50)

                    print(f"\nEl total de la venta antes de impuestos es de ${monto:.2f}")
                    print(f"\nEl cargo generado es de: {IVA}")
                    print(f"\nEl monto total a pagar es : {monto_con_iva:.2f}")
                    print("\nEl listado de la venta es: ")
                    print(f"\nVenta realizada a {cliente} con fecha de {fecha}")
                    print("-" * 55)
                    print("Clave del artículo\tDescripcion\tCantidad\tPrecio Unitario")
                    for detalle in bolsa:
                        print(f"{detalle.folio_unico}\t\t\t{detalle.descripcion}\t\t\t{detalle.cantidad}\t\t${detalle.precio_unitario:.2f}")
                        print("-" * 55)

    if opcion == 4:
        break
