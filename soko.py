mapa = [3,4,4,0,4,4,3]
#definimos la posicion inicial del personaje
posicion colulmna = 3  constant name "posicion_columna" doesn't conform to UPPER_CASE name
#imprime el mapa
print(mapa)
#pide al usuario el movimiento 
movimiento = input("selecciona el movimiento:")

if movimiento == 'd':
    mapa[posicion_columna] = 4#   trailing whitespace
    mapa[posicion_columna + 1] =0
    posicion_columna+=1
