while True:  
    contador = 0
    while contador <= 10:
        print(contador)
        contador = contador + 1
    
    # Descendo de 9 até 1 (para não repetir o 10 nem o 0 na próxima subida)
    contador = 9
    while contador > 0:
        print(contador)
        contador = contador -9