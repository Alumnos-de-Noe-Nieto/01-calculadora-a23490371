# restas.py
"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
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


def validar_restas(cadena: str) -> bool:
    """
    Valida que las restas (sustracciones) sean válidas.
    """
    i = 0

    while i < len(cadena) - 1:
        actual = cadena[i]
        siguiente = cadena[i + 1]

        if VALORES[actual] < VALORES[siguiente]:
            par = cadena[i:i + 2]

            if par not in SUSTRACCIONES_VALIDAS:
                return False

            if i > 0 and cadena[i - 1] == actual:
                return False

            i += 2
        else:
            i += 1

    return True
