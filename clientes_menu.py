from Server_SQL.zona_fit_db.cliente import Cliente
from Server_SQL.zona_fit_db.cliente_dao import ClienteDAO

print("*** Clientes zona fit (GYM) ***")
opcion = None

while opcion != 5:
    print(f"""Menu:
    1. Listar clientes
    2. Agregar clientes
    3. Modificar Clientes
    4. Eliminar clientes
    5. Salir""")
    opcion = int(input("Escribe una opcion: "))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print("--- Lista de clientes ---")
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre_var = input("Nombre: ")
        apellido_var = input("Apellido: ")
        membresia_var = input("Membresia: ")
        clientes = Cliente(nombre=nombre_var,apellido=apellido_var,
                           membresia=membresia_var)
        insertar_cliente = ClienteDAO.insertar(clientes)
        print(f"Cliente agregado: {insertar_cliente}")
    elif opcion == 3:
        id_cliente_var = int(input("Ingrese el valor de id: "))
        nombre_var = input("Ingrese nombre: ")
        apellido_var = input("Ingrese apellido: ")
        membresia_var = int(input("Ingrese la membresia: "))
        cliente = Cliente(id_cliente_var,nombre_var,apellido_var,
                                     membresia_var)
        actualizar_cliente = ClienteDAO.actualizar(cliente)
        print(f"Agregado correctamente :D {actualizar_cliente}")
    elif opcion == 4:
        id_cliente = int(input("Cliente a eliminar: "))
        cliente = Cliente(id=id_cliente)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f"Cliente eliminados: {clientes_eliminados}")
    else:
        print("Salimos de la aplicacion :D")