# orden_descendente.py
"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""

VALORES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

SUSTRACCIONES_VALIDAS = {"IV", "IX", "XL", "XC", "CD", "CM"}


def validar_orden_descendente(cadena: str) -> bool:
    """
    Valida que los símbolos estén en orden descendente de valor (izquierda a derecha).
    """
    if len(cadena) <= 1:
        return True

    i = 0
    valor_anterior = float("inf")

    while i < len(cadena):
        if i + 1 < len(cadena) and VALORES[cadena[i]] < VALORES[cadena[i + 1]]:
            par = cadena[i:i + 2]

            if par not in SUSTRACCIONES_VALIDAS:
                return False

            if i > 0 and cadena[i - 1] == cadena[i]:
                return False

            valor_bloque = VALORES[cadena[i + 1]] - VALORES[cadena[i]]

            if valor_bloque > valor_anterior:
                return False

            valor_anterior = valor_bloque
            i += 2
        else:
            valor_actual = VALORES[cadena[i]]

            if valor_actual > valor_anterior:
                return False

            valor_anterior = valor_actual
            i += 1

    return True
