import unittest
from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart

# def is_connected():
#     return False

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

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.00, discount=11.00)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.00))
        self.shopping_cart_1.add_product(Product(name='Camara', price=700.00, discount=70.00))
        self.shopping_cart_1.add_product(Product(name='PC', price=1000.00, discount=0.00))
        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 2000)
        self.assertEqual(self.shopping_cart_1.total, 1645.00)

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)

    # @unittest.skip('No cumple con los requerimientos necesarios')
    # def test_skip_example(self):
    #     self.assertEqual(1, 1)

    # # skipIf => evalua sobre verdadero
    # # skipUnless => evalua sobre falso (si es falso se salta la prueba)
    # # @unittest.skipIf(is_available_to_skip(), 'No se cuenta con todos los requerimientos')
    # @unittest.skipUnless(is_connected(), 'No se cuenta con todos los requerimientos')
    # def test_skip_example_two(self):
    #     pass

    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.name, 'El codigo no cumple con la expresión')

# if __name__ == '__main__':
#     # To excecute the tests from the shell command like: python -m unittest -v entities.test.test_shopping_cart.TestShoppingCart.test_discount_error
#     # To excecute all the testings we use the next commnad from the package: python -m unittest discover
#     unittest.main()