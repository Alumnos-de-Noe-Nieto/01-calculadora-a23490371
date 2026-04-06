"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos

VALORES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.
    """
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("La cadena contiene símbolos inválidos")

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("La cadena tiene repeticiones inválidas de I/X/C/M")

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("La cadena tiene repeticiones inválidas de V/L/D")

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("La cadena no respeta el orden descendente")

    if not validar_restas(cadena):
        raise ExpresionInvalida("La cadena contiene restas inválidas")

    total = 0
    valor_previo = 0

    for simbolo in reversed(cadena):
        valor_actual = VALORES[simbolo]

        if valor_actual < valor_previo:
            total -= valor_actual
        else:
            total += valor_actual

        valor_previo = valor_actual

    return total