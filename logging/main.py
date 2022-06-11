import logging

# DEBUG = 10 => debug
# INFO = 20 => info
# WARNING = 30 => warning
# ERROR = 40 => error
# CRITICAL = 50 => critical

# To change the default behavior to print messages on terminal
# By default only shows on terminal from WARNING (30)
# logging.basicConfig(level=10)
logging.basicConfig(level=logging.DEBUG)

def suma(numero1: int, numero2: int) -> int:
    """Permite sumar 2 números enteros.

    Args:
        numero1 (int):
        numero2 (int):

    Returns:
        int:
    """
    logging.debug("Entramos aquí!!!!!")
    resultado = numero1 + numero2
    logging.debug("Nos encontramos en está línea")
    return resultado

if __name__ == "__main__":
    logging.debug("Antes del llamado de la función")
    resultado = suma(15, 20)
    logging.info(resultado)