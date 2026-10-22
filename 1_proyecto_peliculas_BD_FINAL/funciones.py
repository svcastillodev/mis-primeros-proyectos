import mysql.connector

def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("...¡Oprima cualquier tecla para continuar!...")
    
def accionExitosa():
    input("...¡Acción Realizada con Éxito!...")

def accionNOExitosa():
    input("...¡No fue posible realizar esta Acción. Inténtalo nuevamente!...")   
    
def terminarSistema():
    input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  Vuelve pronto ::::...")
    
def opcionInvalida():
    input("\n\t.... ¡Opción inválida, vuelve a intentarlo!.... ")


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas_3b"
        )

        return conexion

    except:
        print("...¡No fue posible conectarse a la base de datos!...")
        return None