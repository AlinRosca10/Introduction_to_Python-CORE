# product.py

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} x {self.price:.2f} = {self.total_price():.2f}"

