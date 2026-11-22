from decimal import Decimal, ROUND_HALF_UP

CENTAVOS = Decimal("0.01")


def arredondar(valor):
    return Decimal(valor).quantize(CENTAVOS, rounding=ROUND_HALF_UP)


def formatar_moeda(valor):
    texto = f"{arredondar(valor):,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"
