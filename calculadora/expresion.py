"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    """
    Pipeline completo - Orquestación de todos los niveles.
    """
    tokens = parsear_expresion(expresion)

    if not tokens:
        raise ExpresionInvalida("La expresión está vacía")

    tokens = [token for token in tokens if token.tipo != "ESPACIO"]

    resultado = romano_a_entero(tokens[0].valor)

    i = 1
    while i < len(tokens):
        operador = tokens[i]
        numero = romano_a_entero(tokens[i + 1].valor)

        if operador.tipo == "SUMA":
            resultado += numero
        elif operador.tipo == "RESTA":
            resultado -= numero
        else:
            raise ExpresionInvalida("Operador inválido en la expresión")

        i += 2

    if resultado <= 0:
        raise ExpresionInvalida("El resultado debe ser mayor que cero")

    return resultado
