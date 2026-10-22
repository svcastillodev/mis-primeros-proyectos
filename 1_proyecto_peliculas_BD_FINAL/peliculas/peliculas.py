import funciones
from peliculas import crud
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(conexionBD):
    print("\t\t....:::: AGREGAR PELICULAS ::::...\n")
    nombre=input("Ingresa el nombre: ").upper().strip()
    categoria=input("Ingresa la categoria ").upper().strip()
    clasificacion=input("Ingresa la clasificación: ").upper().strip()
    genero=input("Ingresa el género: ").upper().strip()
    idioma=input("Ingresa el idioma: ").upper().strip()
    #Insertar en la BD
    respuesta=crud.insertar(nombre,categoria, clasificacion, genero, idioma, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()
    
def mostrarPeliculas(conexionBD):
    print("\t\t....:::: MOSTRAR PELICULAS ::::...\n")
    #Consultar en la BD
    pelis=crud.consultar(conexionBD)
    if len(pelis)>0:
        print(f"\t{'Código':<10}\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<20}\t{'Genéro':<15}\t{'Idioma':<10}")
        print(f"-"*110)
        for i in pelis:
            print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<20}\t{i[4]:<15}\t{i[5]:<10}")
        print(f"-"*110)
    else:
        print("No hay películas que mostra por el momento")
    funciones.espereTecla()
   
def limpiarPeliculas(conexionBD):
     print("\t\t....:::: BORRRAS TODAS PELICULAS ::::...\n") 
     opc=""
     while opc!="si" and opc!="no":
        opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()

        if opc=="si":
             respuesta=crud.vaciar(conexionBD)
             if respuesta:
                funciones.accionExitosa()
             else:
                funciones.accionNOExitosa()
        funciones.espereTecla()

    
def buscarPeliculas(conexionBD):
    print("\t\t....:::: BUSCAR PELICULAS ::::....\n")
    nombre = input("Escribe el nombre de la pelicula: ").upper().strip()
    #Buscar en la BD
    pelis= crud.buscar(nombre, conexionBD)
    if len(pelis)>0:
        print(f"\t{'Código':<10}\t{'Nombre':<10}\t{'Categoría':<15}\t{'Clasificación':<10}\t{'Genéro':<15}\t{'Idioma':<10}")
        print(f"-"*100)
        for i in pelis:
            print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<15}\t{i[4]:<15}\t{i[5]:<10}")
        print(f"-"*100)
    else:
        print("...¡No existe esta película. Por favor, verifique!...")
    funciones.espereTecla()

def borrarPeliculas(conexionBD):
    print("\t\t\t\t....:::: BORRAR PELICULAS ::::....\n")
    nombre = input("\n\t\tEscribe el nombre de la pelicula: ").upper().strip()
    pelis= crud.buscar(nombre, conexionBD)
    if len(pelis)>0:
        print(f"\t{'Código':<10}\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<15}\t{'Genéro':<15}\t{'Idioma':<10}")
        print(f"-"*100)
        for i in pelis:
            print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<15}\t{i[4]:<15}\t{i[5]:<10}")
        print(f"-"*100)
        opc=""
        while opc!="si" and opc!="no":
            opc=input("\n\t\t¿Deseas borrar la(s) pelicula(s) (Si/No)? ").lower().strip()
        if opc=="si":
             respuesta=crud.borrar(nombre, conexionBD)
             if respuesta:
                funciones.accionExitosa()
             else:
                funciones.accionNOExitosa()
    else:
        print("\n\t\t...¡No existe esta película. Por favor, verifique!...")
    funciones.espereTecla()


def modificarPeliculas(conexionBD):
    print("\t\t\t\t....:::: MODIFICAR PELICULAS ::::....\n")
    nombre= input("\t\tEscribe el nombre de la pelicula: ").upper().strip()
    pelis= crud.buscar(nombre, conexionBD)
    if len(pelis)>0:
        print(f"\t{'Código':<10}\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<15}\t{'Genéro':<15}\t{'Idioma':<10}")
        print(f"-"*100)
        for i in pelis:
            print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<15}\t{i[4]:<15}\t{i[5]:<10}")
        print(f"-"*100)
        opc=""
        while opc!="si" and opc!="no":
            opc=input("\n\t\t¿Deseas actualizar el nombre de la pelicula (Si/No)? ").lower().strip()
        if opc=="si":
             nuevo_nombre=input("\n\t\tEscribe su nuevo nombre: ").upper().strip()
             categoria=input("Ingresa la  nueva categoria ").upper().strip()
             clasificacion=input("Ingresa la nueva clasificación: ").upper().strip()
             genero=input("Ingresa el  nuevo género: ").upper().strip()
             idioma=input("Ingresa el nuevo idioma: ").upper().strip()
             respuesta=crud.actualizar(nuevo_nombre, categoria, clasificacion, genero, idioma, nombre, conexionBD)
             if respuesta:
                funciones.accionExitosa()
             else:
                funciones.accionNOExitosa()
    else:
        print("\n\t\t...¡No existe esta película. Por favor, verifique!...")
    funciones.espereTecla()

