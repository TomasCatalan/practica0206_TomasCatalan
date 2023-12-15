def linea_tabla_mult():

    n = int(input("Introduce un numero entre 1 y 10"))
    m = int(input("Introduce otro numero (m) entre 1 y 10"))
    
    nombre_fichero = "Tabla-" + str(n) + ".txt"

    try:
        with open(nombre_fichero, 'r') as archivo:
                lineas = archivo.readlines()
                print("Línea " + str(m) + ": " + lineas[m-1].strip())
            
    except FileNotFoundError:
            print("Error: El archivo no existe.")

    return

linea_tabla_mult()