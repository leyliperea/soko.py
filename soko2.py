class Soko:

  def __init__(self):
    self.iconos = {
    0: "🐇",
    1: "🥕",
    2: "🟢",
    3: "🐕",
    4: "⬜",
    }
      

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,3,3,4,4,4,3,3,3],
            [3,3,3,3,4,4,0,4,3],
            [3,3,3,4,4,4,4,3,3],
            [3,3,3,3,4,4,4,3,3],
            [3,3,3,3,4,4,4,3,3],
            [3,3,3,4,4,4,3,3,3],
            [3,3,4,4,3,4,3,3,3],
            [2,4,3,3,3,3,3,3,3],
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna+=1

    def derecha(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento1()

    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()

            # Moverse a la izquerda
            if movimiento == 'a':
              # Movimiento 2: [4,0] -> [0,4]
                if self.mapa[self.personaje_fila][self.personaje_columna -1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
                    # Donde estaba el piso pone al personaje
                    self.mapa[self.personaje_fila][self.personaje_columna -1 ] = 0
                    # Donde estaba el personaje pone el piso
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    # Actualiza la posicion del personaje
                    self.personaje_columna-=1
              #moverse hacia arriba
          #Moverse hacia arriba
            if movimiento == 'w':
                #Movimiento 3: [0,4] -> [4,0]
                 if self.mapa[self.personaje_fila -1][self.personaje_columna] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
                    # Donde estaba el piso pone al personaje
                    self.mapa[self.personaje_fila -1][self.personaje_columna] = 0
                    # Donde estaba el personaje pone el piso
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    # Actualiza la posicion del personaje
                    self.personaje_fila-=1

          #Moverse abajo
            if movimiento == 's':
              #Movimiento 4: [4,0] -> [0,4]
               if self.mapa[self.personaje_fila +1][self.personaje_columna] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
                    #Donde estba el piso pone al personaje
                    self.mapa[self.personaje_fila +1][self.personaje_columna] = 0
                    #Donde estaba el personaje pone el piso
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    #Actualiza la posicion del personaje
                    self.personaje_fila +=1
                 



soko = Soko()
soko.jugar() 
