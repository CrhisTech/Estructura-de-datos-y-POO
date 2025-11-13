import pyodbc

try:
    # Ver drivers instalados (útil para depurar)
    print("Drivers disponibles:", pyodbc.drivers())

    # Opción recomendada: autenticación de Windows
    conexion = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=SistemaVentas;"
        "Trusted_Connection=yes;"
    )

    # Si usas autenticación SQL Server, usa:
    # conexion = pyodbc.connect(
    #     "Driver={ODBC Driver 17 for SQL Server};"
    #     "Server=localhost;"
    #     "Database=SistemaVentas;"
    #     "UID=tu_usuario;"
    #     "PWD=tu_contraseña;"
    # )

    print("Conexión exitosa a la base de datos.")
except pyodbc.Error as e:
    print("Error al conectar a la base de datos:", e)