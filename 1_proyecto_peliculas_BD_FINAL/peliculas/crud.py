def insertar(nombre, categoria, clasificacion, genero, idioma, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()

            cursor.execute(
                "insert into peliculas values (null,%s,%s,%s,%s,%s)",
                (nombre,categoria,clasificacion,genero,idioma)
            )

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False



def consultar(conexionBD):
    try:
        if conexionBD!=None:

            cursor=conexionBD.cursor()
            cursor.execute("select * from peliculas")

            return cursor.fetchall()

        else:
            return []

    except:
        return []



def vaciar(conexionBD):
    try:
        if conexionBD!=None:

            cursor=conexionBD.cursor()
            cursor.execute("truncate table peliculas")

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False



def buscar(nombre, conexionBD):
    try:
        if conexionBD!=None:

            cursor=conexionBD.cursor()

            cursor.execute(
                "select * from peliculas where nombre=%s",
                (nombre,)
            )

            return cursor.fetchall()

        else:
            return []

    except:
        return []



def borrar(nombre, conexionBD):
    try:
        if conexionBD!=None:

            cursor=conexionBD.cursor()

            cursor.execute(
                "delete from peliculas where nombre=%s",
                (nombre,)
            )

            conexionBD.commit()

            return True

        else:
            return False

    except:
        return False



def actualizar(nombre_nuevo,categoria,clasificacion,genero,idioma,nombre_viejo,conexionBD):
    try:
        if conexionBD!=None:

            cursor=conexionBD.cursor()

            cursor.execute(
                "update peliculas set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s where nombre=%s",
                (nombre_nuevo,categoria,clasificacion,genero,idioma,nombre_viejo)
            )

            conexionBD.commit()

            return True

        else:
            return False

    except:
        return False