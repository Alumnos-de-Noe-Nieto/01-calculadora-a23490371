"""
Nivel 2: Validación de repeticiones I/X/C/M.

Los símbolos I, X, C y M pueden repetirse hasta 3 veces consecutivas.
Ejemplos válidos: III, XXX, CCC, MMM
Ejemplos inválidos: IIII, XXXX, CCCC, MMMM
"""

PATRONES_INVALIDOS = ("IIII", "XXXX", "CCCC", "MMMM")


def validar_repeticiones_icxm(cadena: str) -> bool:
    """
    Valida que los símbolos I, X, C, M no se repitan más de 3 veces consecutivas.
    """
    return all(patron not in cadena for patron in PATRONES_INVALIDOS)
