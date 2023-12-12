def tabla_mult_fichero_comp():
    """Función que pide un número entero entre 1 y 10 y guarde en un fichero con el nombre 
    tabla-n.txt la tabla de multiplicar de ese número
    
    Parametros:
        -Numero: un numero entero, entre 1 y 10
        
    Salida:
        - Fichero con la tabla de multiplicar del numero"""
    
    num = int(input("INtroduce un numero entre 1 y 10"))

    nombre_fichero = "Tabla-" + str(num) + ".txt" #La varieable tiene q ser un string

    try:
        with open(nombre_fichero, "r") as fichero:
            for x in range(1,11):

                fichero.read()  #La varieable tiene q ser un string

    except FileNotFoundError:

        print("ERROR: el archivo no existe")

    return

tabla_mult_fichero_comp()