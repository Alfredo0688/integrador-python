from .coneciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
'''

    sql2 = '''
    CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Genero) REFERENCES Genero(ID)
            );
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
        conn = Conneccion()
        conn.cursor.execute(sql2)
        conn.cerrar_con()
    except:
        pass

class PaseoGatos():

    def __init__(self,id_gato,id_paseo,hora_paseo,observaciones,pagado):
       self.id_gato = id_gato
       self.id_paseo = id_paseo
       self.hora_paseo = hora_paseo
       self.observaciones = observaciones
       self.pagado = pagado

    def __str__(self):
        return f'PaseoGatos[{self.id_gato},{self.id_paseo},{self.hora_paseo},{self.observaciones},{self.pagado}]'
    
def guardar_paseo_gato(paseo_gato):
    conn = Conneccion()

    sql= f'''
        INSERT INTO gatos_paseos(id_gato,id_paseo,hora_paseo,observaciones,pagado)
        VALUES('{paseo_gato.id_gato}','{paseo_gato.id_paseo}','{paseo_gato.hora_paseo}','{paseo_gato.observaciones}','{paseo_gato.pagado}');
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al insertar: {e}")

def listar_paseos():
    conn = Conneccion()
    listar_paseos = []

    sql= f'''
        
        SELECT PG.id_gato_paseo, P.fecha, PG.hora_paseo, P.valor_tarifa, 
        G.nombre, P.nombre_paseador, PG.observaciones, PG.pagado FROM gatos AS G INNER JOIN gatos_paseos AS PG 
        ON G.id_gato = PG.id_gato INNER JOIN paseos AS P ON
        PG.id_paseo = P.id_paseo 

        '''
    try:
        conn.cursor.execute(sql)
        listar_paseos = conn.cursor.fetchall()
        conn.cerrar_con()
        #print(listar_paseos)
        return listar_paseos
    except:
        pass
    finally:
        #conn.cerrar_con()
        return listar_paseos

def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql= f'''
        SELECT * FROM Genero;
'''
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except:
        pass

def listar_michis():
    conn = Conneccion()
    listar_michis = []

    sql= f'''
        SELECT * FROM gatos;
'''
    try:
        conn.cursor.execute(sql)
        listar_michis = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_michis
    except:
        pass

def editar_gatos_paseos(gatos_paseos, id):
    conn = Conneccion()

    sql= f'''
        UPDATE gatos_paseos
        SET id_gato = '{gatos_paseos.id_gato}', id_paseo = '{gatos_paseos.id_paseo}', hora_paseo = '{gatos_paseos.hora_paseo}', observaciones = '{gatos_paseos.observaciones}', pagado = '{gatos_paseos.pagado}'
        WHERE id_gato_paseo = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al modificar: {e}")

def borrar_gatos_paseos(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM gatos_paseos
        WHERE id_gato_paseo = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def listar_paseos_cbb():
    conn = Conneccion()
    listar_paseos_lista = []

    sql= f'''
        SELECT * FROM paseos;
'''
    try:
        conn.cursor.execute(sql)
        listar_paseos_lista = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_paseos_lista
    except:
        pass
