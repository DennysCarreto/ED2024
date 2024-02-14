from Node import Empleado, Cliente, Productos, Ventas, Node

class EmpleadoList:
    def __init__(self):
        self.head = None
        self.tamanio = 0

    # Ver si la lista esta vacia
    def list_empty(self):
        return self.head is None

    # Insertar
    def insertarInicio(self, codigo, nombre, contrasenia, usuario):
        # Crear el nodo
        new_node = Empleado(codigo, nombre, contrasenia, usuario)
        # La lista esta vacia(mover head y tail)
        if self.list_empty():
            self.head = new_node
        # La lista tiene al menos un elemento(mover solo el head)
        else:
            new_node.next = self.head
            self.head = new_node
        self.tamanio += 1

    # Imprimir la lista
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.codigo, current.nombre, current.contrasenia, current.usuario, end = '\n')
            current = current.next


 # Buscar por la data
    def find_by(self, codigo):
        current = self.head
        while current is not None:
            if current.codigo == codigo:
                return current.codigo
            else:
                current = current.next
        #return current
        #raise Exception('El elemento no existe')

class LinkedList:
    def __init__(self):
        self.head = None
        self.tamanio = 0

    #Ver si la lista esta vacia
    def list_empty(self):
        return self.head is None

    # Insertar
    def insertIntoEmptyList(self, codigo, name, telefono, correo):
        new_node = Node(codigo, name, telefono, correo)
        self.head = new_node
        self.tamanio = self.tamanio + 1

    def insertar_inicio(self, codigo, name):
        new_nodo = Cliente(codigo, name)
        if self.head is None:
            self.head = new_nodo
            return
        new_nodo.next = self.head
        self.head = new_nodo
        self.tamanio = self.tamanio + 1

# Metodo insertar al final
    def insertarFinal(self, codigo, name, telefono, correo):
        if self.head is None:
            newNode = Node(codigo, name, telefono, correo)
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            newNode = Node(codigo, name)
            current.next = newNode

# insertar en una posicion en especifico
    def insertAntesdePosicion(self, dato, posicion):
        counter = 1
        current = self.head
        while counter < posicion - 1 and current is not None:
            counter += 1
            current = current.next
        if posicion == 1:
            newNode = Node(dato)
            newNode.next = current
            self.head = newNode
        else:
            newNode = Node(dato)
            newNode.next = current.next
            current.next = newNode

# ELIMINAR
    # Eliminar al inicio
    def deleteFromBeginnig (self):
        if self.head is None:
            print('The linked list empty, cannon delete an element')
            return
        else:
            node = self.head
            self.head = self.head.next
            del node        # elimina el nodo

    # Eliminar el ultimo elemento / al final
    def deleteFinal(self):
        if self.head is None:
            print('The linked list empty, cannon an delete')
            return
        else:
            current = self.head
            previous = None
            while current is not None:
                previous = current
                current = current.next
            previous.next = None
            del current
# eliminar en una posicion
    def deleteAtPosition(self, position):
        if self.head is None:
            print('The linked list empty, cannon delete an element')
            return
        else:
            current = self.head
            previous = None
            count = 1
            while current.next is not None and count < position:
                previous = current
                current = current.next
                count += 1
            if current == self.head:
                self.head = current.next
                del current
            else:
                previous.next = current.next
                del current

    def eliminar(self, codigo):
        nodo_actual = self.head

        # Manejar el caso especial cuando el nodo a eliminar es la cabeza
        if nodo_actual is not None:
            if nodo_actual.codigo == codigo:
                self.head = nodo_actual.next
                nodo_actual = None
                return

        # Buscar el nodo a eliminar
        while nodo_actual is not None:
            if nodo_actual.codigo == codigo:
                break
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.next

        # Si el valor no se encontró en la lista
        if nodo_actual == None:
            return

        # Eliminar el nodo
        nodo_anterior.next = nodo_actual.next
        nodo_actual = None

# reemlazar un elemento
    def replaceElement(self, oldElement, newElement):
        current = self.head
        while current is not None:
            if current.data == oldElement:
                current.data = newElement
                break
            current = current.next
# actualizar posicion
    def updateAtPosition(self, newElement, position):
        if self.head is None and position != 1:
            print('No element to update un the linked list')
            return
        elif self.head is None and position == 1:
            newNode = Node(newElement)
            self.head = newNode
            return
        count = 1
        current = self.head
        while current is not None and count < position:
            count += 1
            current = current.next

        if count == position:
            current.data = newElement
        elif current.data is None:
            print('Not enough elements the linked list')

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.nombre, current.codigo, end = ' ')
            current = current.next

    # Buscar en la lista
    def buscar(self, nombre):
        actual = self.head
        while actual:
            if actual.nombre == nombre:
                return actual.nombre
            actual = actual.siguiente
        return None

# Buscar por la data
    def find_by(self, codigo):
        current = self.head
        while current is not None:
            if current.codigo == codigo:
                return current.codigo
            else:
                current = current.next
        #return current
        #raise Exception('El elemento no existe')

