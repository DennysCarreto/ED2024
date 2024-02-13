from LinkedList import LinkedList, EmpleadoList
import os


def submenu():
    print('1 Buscar')
    print('2 Agregar')
    print('3 Eliminar')
    print('4 Modificar')
    print('5 Mostrar datos')
    print('6 Salir')

empleados = EmpleadoList()
empleados.insertarInicio(1010, 'Dennys', 'admin', 'admin')
empleados.insertarInicio(1011, 'Rolando', 'admin2', 'admin2')
print("Lista")
empleados.print_list()
id = int(input("\nIngrese codigo del empleado: "))
res = empleados.find_by(id)
#print(res.codigo)
if res == id:
    print("Acceso Condedio")
    os.system("pause")
    os.system("clear")

else:
    print("El empleado no existe")


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
            print('1 Buscar')

        elif subop == '2':
            print('2 Agregar')
        elif subop == '3':
            print('3 Eliminar')
        elif subop == '4':
            print('4 Modificar')
        elif subop == '5':
            print('5 Mostrar datos')
        elif subop == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        # print('Ver la hora')
        # print(today)

    elif opcion == '2':
        print('**** INVENTARIOS ****')
        submenu()
        subop = input('Seleccione una opcion: ')
        if subop == '1':
            print('1 Buscar')
        elif subop == '2':
            print('2 Agregar')
        elif subop == '3':
            print('3 Eliminar')
        elif subop == '4':
            print('4 Modificar')
        elif subop == '5':
            print('5 Mostrar datos')
        elif subop == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == '3':
        print('**** TURNOS ****')
        # Ver si existe si existe Se le asigna turno else Agregar
        #if codigo == lista.siexiste(): #yomara
        #    print('Si existe, asignando turno')
        #else:
        #    print('No existe, agregar')
        submenu()
        subop = input('Seleccione una opcion: ')
        if subop == '1':
            print('1 Buscar')
        elif subop == '2':
            print('2 Agregar')
        elif subop == '3':
            print('3 Eliminar')
        elif subop == '4':
            print('4 Modificar')
        elif subop == '5':
            print('5 Mostrar datos')
        elif subop == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == '4':
        print("¡Hasta luego!")

        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
