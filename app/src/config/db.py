import pyodbc

try:
    connection = pyodbc.connect(driver='{SQL Server}', server='localhost\SQLEXPRESS', database='Scorreo',               
               trusted_connection='yes')
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)