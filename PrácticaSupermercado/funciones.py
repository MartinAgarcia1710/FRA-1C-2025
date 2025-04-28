#Función para cargar matriz de productos
def cargar_matriz(productos:int) ->list:
    matriz = [["" for x in range(6)] for x in range(productos)]

    for i in range(productos):

        matriz[i][0] = input("Ingrese el nombre del producto")

        for j in range(1, 6):
            matriz[i][j] = int(input(f"stock en sucursal: {j}"))
    
    return matriz


#Función para mostrar matriz de productos
    
def mostrar_matriz(matriz:list, cantidad:int):
    print("Inventario de productos completo")
    
    for x in range(cantidad):
        for y in range(6):
            if y == 0:
                print(matriz[x][y])
            else:
                print("Sucursal", y, ": ", matriz[x][y], "unidades")
        print("")

#Función calculo de stock y prosucto con menor cantidad

def stock_por_producto(matriz:list, cantidad:int):
    menor_stock = None
    nombre_menor_stock = ""
    print("Stock por producto")

    for i in range(cantidad):
        total = 0
        for j in range(1, 6):
            total += matriz[i][j]
        print(matriz[i][0], ":", total, "unidades")

        if (menor_stock is None) or (total < menor_stock):
            menor_stock = total
            nombre_menor_stock = matriz[i][0]

    print(f"Producto menor stock: {nombre_menor_stock} con {menor_stock} unidades")





