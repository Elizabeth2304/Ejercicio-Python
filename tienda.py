
lista_nombres = []
lista_precios = []
lista_cantidad = []
lista_subtotal = []

def menu():
    print("Bienvenidoal pos de venta")
    print("ingrese 1 para iniciar una venta")
    print("ingrese 2 para ver recibo")
    print("ingrese salir para terminar")

def iniciar_venta():
    total = 0
    while True:
        nombre_articulo=input("ingrese el articulo de compra")
        if nombre_articulo == "fin":
            break
        lista_nombres.append(nombre_articulo)
        precio_articulo=float(input("ingrese el precio del articulo"))
        lista_precios.append(precio_articulo)
        cantidad_articulo=float(input("ingrese la catidad comprada"))
        lista_cantidad.append(cantidad_articulo)
        sub_total = precio_articulo * cantidad_articulo
        lista_subtotal.append(sub_total)
        total += sub_total
    return total

while True:
    menu()
    opciones = input()
    match opciones:
        case "1":
            total = iniciar_venta()
            print(f"El total de la venta es {total}")
        case "2":
            print("********************************")
            print("producto cantidad valor total")
            for i in range(len(lista_nombres)):
                print(f"{lista_nombres[i]} {lista_cantidad[i]}  {lista_precios[i]}  {lista_subtotal[i]}")
                print(f"El total de la venta es {total}")
        case "salir" | "stop":
            break
        case _:
            print("opcion no valida")