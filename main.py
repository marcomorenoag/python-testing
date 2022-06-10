"""Este es el Docstring dl módulo main."""

class User:
    """Permite representar un usuario."""
    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User.

        Args:
            username (str): El username del usuario.
            password (str): El password del usuario.
        """
        pass


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es o no un palindromo.

    Args:
        sentence (str): Cadena a evaluar.

    Returns:
        bool: True o False.

    Examples:

    >>> palindromo('Anita lava la tina')
    True
    
    >>> palindromo('CodigoFacilito')
    False
    
    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
