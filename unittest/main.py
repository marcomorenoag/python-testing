# # assert

# if __name__ == '__main__':
#     try:
#         # assert 5 == 10, 'Lo sentimos, 5 no es igual a 10'
#         if not 5 == 10:
#             raise AssertionError('Lo sentimos, 5 no es igual a 10')
#         print("El programa continua con su ejecución")
#     except AssertionError as error:
#         print(error)

def suma_numeros_positivos(n1: int, n2: int) -> int:
    """Permite sumar dos numeros enteros positivos

    Args:
        n1 (int)
        n2 (int)

    Returns:
        int
    """
    assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar numeros positivos'
    return n1 + n2


if __name__ == '__main__':
    try:
        resultado = suma_numeros_positivos(-10, 20)
        print(resultado)
    except AssertionError as error:
        print(error)