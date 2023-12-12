def tabla_mult_fichero():
    """Función que pide un número entero entre 1 y 10 y guarde en un fichero con el nombre 
    tabla-n.txt la tabla de multiplicar de ese número
    
    Parametros:
        -Num: un numero entero, entre 1 y 10
        
    Salida:
        - Fichero con la tabla de multiplicar del numero"""
    
    num = int(input("INtroduce un numero entre 1 y 10"))

    nombre_fichero = "Tabla del" + num + ".txt"

    print(nombre_fichero)

tabla_mult_fichero()