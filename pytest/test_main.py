
# Ejecutar todas las pruebas: pytest -v
# Ejecutar pruebas de una clase puntual: pytest -v test_main.py::TestExample
# Ejecutar prueba puntutal: pytest -v test_main.py::TestExample::test_resta_dos_numeros
class TestExample():
    
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Lo sentimos, la suma no es correcta.'

    def test_resta_dos_numeros(self):
        assert 10 - 10 == 0, 'Lo sentimos, la resta no es correcta.'

class TestExample2():

    def test_multiplicacion_dos_numeros(self):
        assert 2 * 10 == 20, 'Lo sentimos, la multiplicacion no es correcta.'