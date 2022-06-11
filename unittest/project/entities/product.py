class ProductDiscountError(Exception):
    """Custom error

    Args:
        Exception (_type_): _description_
    """
    pass

class Product:
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        if discount > price:
            raise ProductDiscountError("El descuento no puede ser mayor que el precio")
        self.discount = discount

    @property
    def code(self):
        return f'code-{self.name}'