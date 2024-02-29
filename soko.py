"""
1-Cajas
2-Metas
3-Paredes
4-Piso
5-Personaje meta
6-caja meta
"""


#define el mapa de juego
mapa = [3,4,4,0,4,4,3]
#definimos la posicion inicial del personaje
posicion colulmna = 3  constant name "posicion_columna" doesn't conform to UPPER_CASE name
#imprime el mapa
print(mapa)
#pide al usuario el movimiento 
movimiento = input("selecciona el movimiento:")

if movimiento == 'd':
    #movimiento 1: [0,4] -> [4,0]
    if mapa [posicion_columna] == 0 and mapa [posicion_columna+1] ==4:
        #donde estaba el persona pone un piso
        mapa[posicion_columna] = 4 
        #donde estaba el piso pone el personaje
        mapa[posicion_columna + 1] = 0
        #actualiza la posicion del personaje
        posicion_columna+=1
# moverse a la izquierda 
    if movimiento =='a':
       #movimiento 2: [4,0] -> [0,4]
        if mapa[posicion_columna-1] ==4 and mapa [posicion_columna] ==0:
            mapa[posicion_columna-1] = 0
            mapa[posicion_columna] = 4
            posicion_columna-=1
        
