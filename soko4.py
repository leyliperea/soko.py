class Soko:
  niveles = [
      [
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 0, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 4, 4, 4, 4, 4, 4, 4, 4, 3],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
      ],
      [
          # Definir el segundo nivel aquí
          # ...
      ]
  ]

  def __init__(self, nivel):
      # Define el mapa del nivel seleccionado
      self.mapa = self.niveles[nivel]

      # Encuentra la posición inicial del personaje en el nivel
      for i in range(len(self.mapa)):
          for j in range(len(self.mapa[0])):
              if self.mapa[i][j] == 0:
                  self.personaje_fila = i
                  self.personaje_columna = j
                  return

  def imprimir_mapa(self):
      for fila in self.mapa:
          print(fila)

  def derecha(self):
      if self.mapa[self.personaje_fila][self.personaje_columna] == 0:
          # Si el siguiente espacio es una caja, intenta empujarla
          if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
              self.movimiento1()
              self.personaje_columna += 1
          # Si el siguiente espacio es un objetivo, empuja la caja al objetivo
          elif self.mapa[self.personaje_fila][self.personaje_columna + 1] == 5:
              self.movimiento5()
              self.personaje_columna += 1

  def izquierda(self):
      if self.mapa[self.personaje_fila][self.personaje_columna] == 0:
          if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
              self.movimiento2()
              self.personaje_columna -= 1
          elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5:
              self.movimiento6()
              self.personaje_columna -= 1

  def arriba(self):
      if self.mapa[self.personaje_fila][self.personaje_columna] == 0:
          if self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
              self.movimiento3()
              self.personaje_fila -= 1
          elif self.mapa[self.personaje_fila - 1][self.personaje_columna] == 5:
              self.movimiento7()
              self.personaje_fila -= 1

  def abajo(self):
      if self.mapa[self.personaje_fila][self.personaje_columna] == 0:
          if self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
              self.movimiento4()
              self.personaje_fila += 1
          elif self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5:
              self.movimiento8()
              self.personaje_fila += 1

  def movimiento1(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

  def movimiento2(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

  def movimiento3(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

  def movimiento4(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

  def movimiento5(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

  def movimiento6(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

  def movimiento7(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

  def movimiento8(self):
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

  def jugar(self):
      while True:
          self.imprimir_mapa()
          movimiento = input("Selecciona el movimiento d (derecha), a (izquierda), w (arriba), s (abajo): ")
          if movimiento == 'd':
              self.derecha()
          elif movimiento == 'a':
              self.izquierda()
          elif movimiento == 'w':
              self.arriba()
          elif movimiento == 's':
              self.abajo()


def elegir_nivel():
  while True:
      try:
          nivel = int(input("Selecciona el nivel (1, 2, etc.): "))
          if nivel < 1 or nivel > len(Soko.niveles):
              print("Por favor, selecciona un nivel válido.")
          else:
              return nivel - 1  # El índice de la lista es nivel - 1
      except ValueError:
          print("Entrada no válida. Por favor, ingresa un número entero.")


nivel_elegido = elegir_nivel()
soko = Soko(nivel_elegido)
soko.jugar()
