# Sokoban
Programar el juego sokoban en una versión retro consola.

## 0. Objetivo

## 1. Reglas del juego

El juego sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar totas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando numeros para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

mapa = [
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,4,4,4,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,1,4,4,2,2,2,2,2,3,3,3,3,3,3],
          [3,3,3,3,3,4,4,1,2,2,2,2,2,2,2,3,3,3,3],
          [3,3,3,4,4,1,4,1,4,4,4,4,4,4,4,4,4,4,3],
          [3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,3,3,3],
          [3,3,3,3,3,4,0,4,4,2,4,4,4,4,4,4,4,4,3],
          [3,3,3,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,4,3,4,3,3,4,3,3,3,3,3,3,3,3,3,3],
          [3,4,4,4,3,4,3,3,4,3,3,3,3,3,4,4,4,4,3],
          [3,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3],
          [3,3,3,3,3,4,3,3,3,4,3,4,3,3,4,4,4,4,3],
          [3,3,3,3,3,4,4,4,4,4,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    ]

### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje meta
- 6 - Caja meta
- 7 - Segundo personaje

## 3. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover.

- a -> Izquierda
- d -> Derecha
- w -> Arriba
- s -> Abajo

## 4. Función a implementar

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | ✔ |  |
| 1. | Repetir el juego hasta terminar el nivel. | ✔ |  | | - |
| 2. | Imprimir mapa.| ✔ |  |
| 3. | Leer el movimiento. | ✔ |  |
| 4. | Evaluar el movimiento del usuario. | ✔ |  |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | ✔ | [0,4] | [4,0] | |
| 6. | Personaje, meta  | ✔ | [0,2] | [4,6] |  |
| 7. | Personaje, caja, pasillo | ✔ | [0,1,4] | [4,0,1] |  |
| 8. | Personaje, caja,  meta | ✔ | [0,1,2] | [4,0,6] |  |
| 9. | Personaje, caja_meta, pasillo | ✔ | [0,6,4] | [4,5,1] |  |
| 10. |Personaje, caja_meta, meta | ✔ | [0,6,2] | [4,5,6] |  |
| 11. | Personaje_meta, pasillo | ✔ | [5,4] | [2,0] |  |
| 12. | Personaje_meta, meta | ✔ | [5,2] | [2,5] |  |
| 13. | Personaje_meta, caja, pasillo | ✔ | [5,1,4] | [2,0,1] |  |
| 14. | Personaje_meta, caja, meta | ✔ | [5,1,2] | [2,0,6] |  |
| 15. | Personaje_meta, caja_meta, pasillo | ✔ | [5,6,4] | [2,5,1] |  |
| 16. | Personaje_meta, caja_meta, meta | ✔ | [5,6,2] | [2,5,6] |  |

## Izquierda

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 17. | Personaje y espacio | ✔ |  |
| 18. | Personaje y meta | ✔ |  |
| 19. | Personaje, caja y espacio | ✔ |  |
| 20. | Personaje, caja y meta | ✔ |  |
| 21. | Personaje, caja_meta y espacio | ✔ |  |
| 22. | Personaje, caja_meta y meta | ✔ |  |
| 23. | Personaje_meta y espacio | ✔ |  |
| 24. | Personaje_meta y meta | ✔ |  |
| 25. | Personaje_meta, caja y espacio | ✔ |  |
| 26. | Personaje_meta, caja y meta | ✔ |  |
| 27. | Personaje_meta, caja_meta y espacio | ✔ |  |
| 28. | Personaje_meta, caja_meta y meta | ✔ |  |

## Arriba

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 29. | Personaje y espacio | ✔ |  |
| 30. | Personaje y meta | ✔ |  |
| 31. | Personaje, caja y espacio | ✔ |  |
| 32. | Personaje, caja y meta | ✔ |  |
| 33. | Personaje, caja_meta y espacio | ✔ |  |
| 34. | Personaje, caja_meta y meta | ✔ |  |
| 35. | Personaje_meta y espacio | ✔ |  |
| 36. | Personaje_meta y meta | ✔ |  |
| 37. | Personaje_meta, caja y espacio | ✔ |  |
| 38. | Personaje_meta, caja y meta | ✔ |  |
| 39. | Personaje_meta, caja_meta y espacio | ✔ |  |
| 40. | Personaje_meta, caja_meta y meta | ✔ |  |

## Abajo

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 41. | Personaje y espacio | ✔ |  |
| 42. | Personaje y meta | ✔ |  |
| 43. | Personaje, caja y espacio | ✔ |  |
| 44. | Personaje, caja y meta | ✔ |  |
| 45. | Personaje, caja_meta y espacio | ✔ |  |
| 46. | Personaje, caja_meta y meta | ✔ |  |
| 47. | Personaje_meta y espacio | ✔ |  |
| 48. | Personaje_meta y meta | ✔ |  |
| 49. | Personaje_meta, caja y espacio | ✔ |  |
| 50. | Personaje_meta, caja y meta | ✔ |  |
| 51. | Personaje_meta, caja_meta y espacio | ✔ |  |
| 52. | Personaje_meta, caja_meta y meta | ✔ |  |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  |  | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  |  |  |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (Fusión del personaje asi como la transformación del personaje en una caja). |  |  |
