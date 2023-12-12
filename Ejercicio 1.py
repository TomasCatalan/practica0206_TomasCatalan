def tabla_mult_fichero():
    """Función que pide un número entero entre 1 y 10 y guarde en un fichero con el nombre 
    tabla-n.txt la tabla de multiplicar de ese número
    
    Parametros:
        -Numero: un numero entero, entre 1 y 10
        
    Salida:
        - Fichero con la tabla de multiplicar del numero"""
    
    num = int(input("INtroduce un numero entre 1 y 10"))

    nombre_fichero = "Tabla-" + str(num) + ".txt" #La varieable tiene q ser un string

    with open(nombre_fichero, "w") as fichero:
        for x in range(1,11):

            fichero.write(str(num) + " * " + str(x) + "\n")  #La varieable tiene q ser un string

    return

tabla_mult_fichero()
