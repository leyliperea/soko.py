# soko.py
juegocodigos
descripcion del juego sokoban

##factores
1-Cajas
2-Metas
3-Paredes
4-Piso
5-Personaje meta
6-caja meta

##1.-Reglas del juego
1.El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2.El personaje solo puede empujar 1 caja en cualquier sentido.
3.El personaje se moverá en un mapa predefinido.
4.Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.

## 2 elementos del jugo
2.0 Mapa de juego
Cada nivel del juego se colocará dentro de una matriz bidimensional, colocando números para representar los elementos del juego, a continuación se tiene un ejemplo básico de nivel.

##3controles
Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia donde se quiere mover.

a -> Izquierda
s -> Derecha
w -> Arriba
s -> Abajo
##mapa = [
[3,3,3,3,3], 
[3,4,4,4,3], 
[3,4,0,4,3], 
[3,4,4,4,3], 
[3,3,3,3,3]
]
## 4
No| descripcion                 | inicia|termina
1 |mover derecha y piso         |       |
2 |mover izquierda, piso        |       |
3 |mover derecha, caja, piso    |       |
4 |                             |       |
5 |                             |       |
6 |
