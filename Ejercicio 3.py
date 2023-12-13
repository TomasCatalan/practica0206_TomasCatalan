def linea_tabla_mult():

    n = int(input("Introduce un numero entre 1 y 10"))
    m = int(input("Introduce otro numero (m) entre 1 y 10"))
    
    nombre_fichero = "Tabla-" + str(n) + ".txt"

    with open(nombre_fichero, "w") as fichero:
        for x in range(1,11):

            fichero.write(str(n) + " * " + str(x) + "\n")

    try:
        with open(nombre_fichero, 'r') as archivo:
                lineas = archivo.readlines()
                print("Línea " + str(m) + ": " + lineas[m-1].strip())
            
    except FileNotFoundError:
            print("Error: El archivo no existe.")

    return

linea_tabla_mult()