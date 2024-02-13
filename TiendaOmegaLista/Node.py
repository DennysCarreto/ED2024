class Empleado:
    def __init__(self, codigo, nombre, contrasenia, usuario):
        self.codigo = codigo
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.usuario = usuario
        self.next = None

class Cliente:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.next = None

class Productos:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia
        self.next = None

class Ventas:
    def __init__(self, codigo, nombre, precio, cantidad, total):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.total = total
        self.next = None

class Node:
    def __init__(self, codigo, name, telefono, correo):
        self.codigo = codigo
        self.name = name
        self.telefono = telefono
        self.correo = correo
        self.next = None

