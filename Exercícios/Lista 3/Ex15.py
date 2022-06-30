def desenhos():
  def desenharPiramide(n):
    for i in range (1, n+1):
      print(i * "*")
  desenharPiramide(6)
  
  print( )
  
  def desenharPiramideInvertida(n):
    for i in range (n, 0, -1):
      print(i * "*")
  desenharPiramideInvertida(6)

  print( )

  def desenharDiagonal(n):
    for i in range (1, n+1):
      print( i * " ","*")
  desenharDiagonal(6)

  print( )
  
  def desenharDiagonalInvertida(n):
    for i in range (n, 0, -1):
      print( i * " ","*")
  desenharDiagonalInvertida(6)
  print( )

  def piramideAnguloReto(n):
    for i in range (n, 0, -1):
      print((n-i)*" ", i * "*")
  piramideAnguloReto(6)

  print( )
  
  def piramideAnguloRetoInvertida(n):
    for i in range (n+1):
      print((n-i) * " ", i * "*")
  piramideAnguloRetoInvertida(6)

  print( )

  def losangos(n):
    for i in range(n+1):
      print(i * " ", n * "* ")
  losangos(6)

  print( )

  def triangulo(n):
    for i in range(n, 0, -1):
      print((n-i) * " ", i * "* ")
  triangulo(6)

  print( )
  def diagonaisDuplas(n):
    pass
desenhos()