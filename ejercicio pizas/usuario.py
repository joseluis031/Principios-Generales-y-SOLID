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
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nDireccion: {self.direccion}\nTelefono: {self.telefono}\nTarjeta: {self.tarjeta}\nPedidos: {self.pedidos}"
    
    def __repr__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nDireccion: {self.direccion}\nTelefono: {self.telefono}\nTarjeta: {self.tarjeta}\nPedidos: {self.pedidos}"