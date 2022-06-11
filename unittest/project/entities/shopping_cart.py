from typing import List
from entities.product import Product


class ShoppingCart:
    def __init__(self) -> None:
        self.__products: List[Product] = [] # Private field

    def empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self) -> bool:
        return not self.empty()

    def add_product(self, product) -> None:
        self.__products.append(product)

    # Convert method to attribute
    @property
    def products(self) -> List[Product]:
        return self.__products.copy()

    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)

    @property
    def total(self) -> float:
        return sum([(product.price-product.discount) for product in self.__products])
