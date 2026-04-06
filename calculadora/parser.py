"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str
    valor: str
    posicion: int


ROMANOS = set("IVXLCDM")


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.
    """
    if expresion.strip() == "":
        return []

    tokens = tokenizar_expresion(expresion)

    if not validar_estructura_tokens(tokens):
        raise ExpresionInvalida(
            f'La expresión "{expresion}" tiene una estructura inválida'
        )

    return tokens


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza una expresión de texto en una lista de tokens.
    """
    tokens = []
    i = 0

    while i < len(expresion):
        caracter = expresion[i]

        if caracter == " ":
            tokens.append(Token("ESPACIO", " ", i))
            i += 1
        elif caracter == "+":
            tokens.append(Token("SUMA", "+", i))
            i += 1
        elif caracter == "-":
            tokens.append(Token("RESTA", "-", i))
            i += 1
        elif caracter in ROMANOS:
            inicio = i

            while i < len(expresion) and expresion[i] in ROMANOS:
                i += 1

            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{expresion[i]}' en posición {i}")

    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida que la expresión tenga una estructura válida.
    """
    tokens_filtrados = [t for t in tokens if t.tipo != "ESPACIO"]

    if len(tokens_filtrados) < 3:
        return False

    if len(tokens_filtrados) % 2 == 0:
        return False

    if tokens_filtrados[0].tipo != "ROMANO":
        return False

    if tokens_filtrados[-1].tipo != "ROMANO":
        return False

    for i, token in enumerate(tokens_filtrados):
        if i % 2 == 0:
            if token.tipo != "ROMANO":
                return False
        else:
            if token.tipo not in {"SUMA", "RESTA"}:
                return False

    return True