from LinkedList import LinkedList, EmpleadoList


def submenu():
    print('1 Agregar')
    print('2 Buscar')
    print('3 Eliminar')
    print('4 Modificar')
    print('5 Mostrar datos')
    print('6 Salir')

empleados = EmpleadoList()
empleados.insertarInicio(1010, 'Dennys', 'admin', 'admin')
empleados.insertarInicio(1011, 'Rolando', 'admin2', 'admin2')
print("Lista")
empleados.print_list()
satisfactorio = 0
while True:
    id = int(input("\nIngrese codigo del empleado: "))
    res = empleados.find_by(id)
    if res == id:
        satisfactorio = 1
        print("Acceso Condedio")
        print("\n BIENVENIDO A TIENDA OMEGA")
        print("1. Clientes")
        print("2. Productos")
        print("3. Ventas")
        print("4. Salir")

        # Declaramos el objeto de tipo lista
        Clientes = LinkedList()
        Productos = LinkedList()
        Ventas = LinkedList()

        while True:
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                print('****** CLIENTES ******')
                submenu()
                subop = input('Seleccione una opcion: ')
                if subop == '1':
                    print(' Agregar')
                    codigo = input('Inserte codigo del cliente: ')
                    nombre = input('Ingrese nombre del cliente: ')
                    Clientes.insertar_inicio(codigo, nombre)
                    print('Lista Clientes')
                    Clientes.print_list()
                elif subop == '2':
                    print('Buscar')
                    busqueda = input('Ingrese el codigo del cliente para buscar: ')
                    res = Clientes.find_by(busqueda)
                    print('La busqueda es: ', res)
                elif subop == '3':
                    print('Eliminar')
                    codigo = input('Ingrese del codigo del cliente a eliminar: ')
                    Clientes.eliminar(codigo)
                    print('Lista Clientes actualizada')
                    Clientes.print_list()
                elif subop == '4':
                    print('Modificar')

                elif subop == '5':
                    print('5 Mostrar datos')
                    print('Datos de la lista Clientes')
                    Clientes.print_list()
                elif subop == '6':
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                # print('Ver la hora')
                # print(today)

            elif opcion == '2':
                print('**** PRODUCTOS ****')
                submenu()
                subop = input('Seleccione una opcion: ')
                if subop == '1':
                    print('Agregar')
                    codigo = input('Inserte codigo: ')
                    nombre = input('Ingrese nombre: ')
                    precio = input('Ingrese precio: ')
                    existencia = input('Inserte cantidad en existencia: ')
                    Productos.insertar_inicio(codigo, nombre, precio, existencia)
                    print('Lista Clientes')
                    Productos.print_list()
                elif subop == '2':
                    print('Buscar')
                    busqueda = input('Ingrese el codigo para buscar: ')
                    res = Productos.find_by(busqueda)
                    print('La busqueda es: ', res)
                elif subop == '3':
                    print('Eliminar')
                    codigo = input('Ingrese el codigo a eliminar: ')
                    Productos.eliminar(codigo)
                    print('Lista Productos actualizada')
                    Productos.print_list()
                elif subop == '4':
                    print('Modificar')
                elif subop == '5':
                    print('Mostrar datos')
                    print('Datos de la lista Productos')
                    Productos.print_list()
                elif subop == '6':
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            elif opcion == '3':
                print('**** VENTAS ****')
                submenu()
                subop = input('Seleccione una opcion: ')
                if subop == '1':
                    print('1 Buscar')
                    busqueda = input('Ingrese codigo de venta: ')
                    res = Ventas.find_by(busqueda)
                    print('La venta es: ', res)
                elif subop == '2':
                    print('2 Agregar/Venta')
                    codigo = input('Ingrese codigo de producto: ')
                    nombre = input("Ingrese nombre de producto: ")
                    cantidad = int(input("Ingrese la cantidad: "))
                    precio = int(input("Ingrese el precio: "))
                    total = 0
                    total = cantidad * precio
                    descuento = 0
                    if total > 500:
                        descuento = total * 0.15
                    elif total > 300:
                        descuento = total * 0.05
                    Ventas.insertar_inicio(codigo, nombre, precio, cantidad, total)
                    print('Lista de ventas: ')
                    Ventas.print_list()

                elif subop == '3':
                    print('3 Eliminar')
                elif subop == '4':
                    print('Mostrar datos')
                elif subop == '5':
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            elif opcion == '4':
                print("¡Hasta luego!")

                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    elif satisfactorio == 0:
        print('Adios')
        break
    else:
        print("El empleado no existe. Intente de nuevo...")
        print('Ingrese 1 para salir')
