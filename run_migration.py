#!/home/vladimir/Documents/EFISYS/dev/safi-migracion-deploy/.safi_migracion/env/bin/python3
from pathlib import Path
import mysql.connector
from mysql.connector import errorcode
pathlist = Path('.safi_migracion/microfin').glob('**/MIG*.sql')
for path in pathlist:
     # because path is object not string
     file = open(str(path),mode='r')
     sql=file.read()
     file.close
     print(sql)


# verificar si existe archivo de configuración
    -- si no existe solicitar los datos para  crearla

# Realizar conexion
# Ejecutar la carga de los scripts
$




class  migration()

    def connect(self):
        '''
        Devuelve un objeto de  conexión con la Base de datos
        '''
        success_connection=False
        try:
            db_connection=mysql.connector.connect(**self.db_strcon)
            message="MySQL: Database connection is open."
            success_connection=True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                message="MySQL: Authentication failed, wrong username or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                message="MySQL: The database [" +  self.db_name +  "] don't exists"
            else:
                message=err
            return None
        else:
        #     db_connection.close()
        return db_connection #success_connection