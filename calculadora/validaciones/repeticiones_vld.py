"""
Nivel 3: Validación de repeticiones V/L/D.

Los símbolos V, L y D NO pueden repetirse.
Ejemplos válidos: V, L, D, MCMXCIV
Ejemplos inválidos: VV, LL, DD
"""

PATRONES_INVALIDOS = ("VV", "LL", "DD")


def validar_repeticiones_vld(cadena: str) -> bool:
    """
    Valida que los símbolos V, L y D no se repitan (máximo 1).
    """
    return all(patron not in cadena for patron in PATRONES_INVALIDOS)
