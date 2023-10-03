class Pedido:
    def __init__(self, id, cliente, producto, cantidad):
        self.id = id
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad

    def __str__(self):
        return f"Pedido: {self.id} - {self.cliente} - {self.producto} - {self.cantidad}"