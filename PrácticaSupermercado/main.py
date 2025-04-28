import funciones

cantidad_productos = 3

matriz_productos = [["" for i in range(6)] for i in range(cantidad_productos)]

#Caragar matriz de productos

matriz_productos = funciones.cargar_matriz(cantidad_productos)

#mostrar matriz de productos
funciones.mostrar_matriz(matriz_productos, cantidad_productos)

#mostrar stock total de todos los productos y producto con menor stock

funciones.stock_por_producto(matriz_productos, cantidad_productos)




