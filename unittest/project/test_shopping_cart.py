import unittest
from product import Product
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Metodo de clase"""
        # print('El metodo de clase setUpClass se ejecuta antes de todas las pruebas')
        pass
    
    @classmethod
    def tearDownClass(cls):
        """Metodo de clase"""
        # print('El metodo de clase tearDownClass se ejecuta despues de todas las pruebas')
        pass

    def setUp(self) -> None:
        # print("El metodo setUp se ejecuta antes de cada una de las pruebas")
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price) # Se crea antes de c/u de las pruebas unitarias
        self.shopping_cart_1 = ShoppingCart() 
        self.shopping_cart_2 = ShoppingCart() 
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self) -> None:
        # print("El metodo tearDown se ejecuta despues de cada una de las pruebas")
        pass

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo sentimos el precio no es el mismo')

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)
    
    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Carrito de compras no está vacío')

    def test_shopping_cart_has_products(self):
        self.assertTrue(self.shopping_cart_2.has_products(), 'Carrito no tiene elementos')
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

if __name__ == '__main__':
    unittest.main()