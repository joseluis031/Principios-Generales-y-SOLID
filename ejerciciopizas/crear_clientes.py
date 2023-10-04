import csv
import random
import string

# Lista de nombres y apellidos ficticios sin tildes
nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofia", "Javier", "Marta"]
apellidos = ["Gonzalez", "Rodriguez", "Lopez", "Fernandez", "Martinez", "Perez", "Gomez", "Diaz", "Sanchez", "Torres"]

# Clase Usuario
class Usuario:
    def __init__(self, nombre, apellido, id, email, password, direccion, telefono, tarjeta, pedidos):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.email = email
        self.password = password
        self.direccion = direccion
        self.telefono = telefono
        self.tarjeta = tarjeta
        self.pedidos = pedidos

# Función para generar un ID aleatorio
def generar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Función para generar datos aleatorios de Usuario
def generar_usuario():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    id = generar_id()
    email = f"{nombre.lower()}.{apellido.lower()}@example.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    direccion = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    telefono = ''.join(random.choices(string.digits, k=10))
    tarjeta = ''.join(random.choices(string.digits, k=16))
    pedidos = random.randint(1, 10)
    return Usuario(nombre, apellido, id, email, password, direccion, telefono, tarjeta, pedidos)

# Generar datos de usuarios y escribir en el archivo CSV
with open('clientes.csv', 'w', newline='') as csvfile:
    fieldnames = ['nombre', 'apellido', 'id', 'email', 'password', 'direccion', 'telefono', 'tarjeta', 'pedidos']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()

    for _ in range(100):
        usuario = generar_usuario()
        writer.writerow({
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'id': usuario.id,
            'email': usuario.email,
            'password': usuario.password,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'tarjeta': usuario.tarjeta,
            'pedidos': usuario.pedidos
        })

print("Base de datos generada con nombres y apellidos ficticios.")
