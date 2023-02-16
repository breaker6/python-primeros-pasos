#Listas
edadesLista = [15, 16 , 18]
nombres = ["Antonio", "Adrian", "Alejandro"]
#Añadir elemento a lista
nombres.append("Kiko")
#Añadir elemento a lista en posición determinada (los elementos posteriores correran una posicion)
nombres.insert(0, "Eustaquio")
#Eliminar elemento de lista (los elementos posteriores retrocederán una posición)
nombres.remove("Antonio")
#Vaciamos la lista
nombres.clear()


#Tuplas (las tuplas a diferencia de las listas son inmutables)
edadesTupla = (14, 15, 21)
#Acceder a un elemento de la tupla
edad = edadesTupla[0]
#Ver longitud de tupla
longitud = len(edad)


#Diccionarios (los elementos del diccionario están compuestos por un indice y un valor)
edadesDiccionario = {"Antonio": 15, "Adrian": 16, "Alejandro": 18}
#Acceder a un elemento del diccionario y dar un error si no lo encuentra
print(edadesDiccionario.get("Antonio", "No se encuentra la edad"))
