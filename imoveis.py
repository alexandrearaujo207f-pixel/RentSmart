from decimal import Decimal

from utilitarios import arredondar


class Imovel:
    TIPO = "Imóvel"
    ALUGUEL_BASE = Decimal("0.00")
    ADICIONAL_2_QUARTOS = Decimal("0.00")
    VALOR_GARAGEM = Decimal("300.00")

    def __init__(self, dois_quartos=False, garagem=False):
        self.dois_quartos = dois_quartos
        self.garagem = garagem

    def adicionais(self):
        itens = []
        if self.dois_quartos:
            itens.append(("Segundo quarto", self.ADICIONAL_2_QUARTOS))
        if self.garagem:
            itens.append(("Vaga de garagem", self.VALOR_GARAGEM))
        return itens

    def subtotal(self):
        total = self.ALUGUEL_BASE
        for _, valor in self.adicionais():
            total += valor
        return total

    def desconto(self):
        return Decimal("0.00")

    def rotulo_desconto(self):
        return ""

    def aluguel_mensal(self):
        return arredondar(self.subtotal() - self.desconto())

    def detalhes(self):
        quartos = "2 quartos" if self.dois_quartos else "1 quarto"
        garagem = "com garagem" if self.garagem else "sem garagem"
        return [quartos, garagem]

    def descricao(self):
        return f"{self.TIPO} ({', '.join(self.detalhes())})"

    def __str__(self):
        return self.descricao()


class Apartamento(Imovel):
    TIPO = "Apartamento"
    ALUGUEL_BASE = Decimal("700.00")
    ADICIONAL_2_QUARTOS = Decimal("200.00")
    DESCONTO_SEM_CRIANCAS = Decimal("0.05")

    def __init__(self, dois_quartos=False, garagem=False, tem_criancas=True):
        super().__init__(dois_quartos, garagem)
        self.tem_criancas = tem_criancas

    def desconto(self):
        if not self.tem_criancas:
            return arredondar(self.subtotal() * self.DESCONTO_SEM_CRIANCAS)
        return Decimal("0.00")

    def rotulo_desconto(self):
        return "Desconto de 5% (sem crianças)" if not self.tem_criancas else ""

    def detalhes(self):
        criancas = "com crianças" if self.tem_criancas else "sem crianças"
        return super().detalhes() + [criancas]


class Casa(Imovel):
    TIPO = "Casa"
    ALUGUEL_BASE = Decimal("900.00")
    ADICIONAL_2_QUARTOS = Decimal("250.00")


class Estudio(Imovel):
    TIPO = "Estúdio"
    ALUGUEL_BASE = Decimal("1200.00")
    PACOTE_VAGAS = Decimal("250.00") 
    VAGAS_NO_PACOTE = 2
    VAGA_EXTRA = Decimal("60.00")

    def __init__(self, vagas=0):
        super().__init__(dois_quartos=False, garagem=False)
        if vagas != 0 and vagas < self.VAGAS_NO_PACOTE:
            raise ValueError("O estacionamento do estúdio começa com 2 vagas.")
        self.vagas = vagas

    def adicionais(self):
        itens = []
        if self.vagas >= self.VAGAS_NO_PACOTE:
            itens.append(("Pacote de 2 vagas", self.PACOTE_VAGAS))
            extras = self.vagas - self.VAGAS_NO_PACOTE
            if extras > 0:
                itens.append((f"{extras} vaga(s) adicional(is) x R$ 60,00",
                              self.VAGA_EXTRA * extras))
        return itens

    def detalhes(self):
        if self.vagas == 0:
            return ["sem estacionamento"]
        return [f"{self.vagas} vagas de estacionamento"]
